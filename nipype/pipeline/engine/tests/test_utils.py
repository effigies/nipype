# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""Tests for the engine utils module
"""
from __future__ import (print_function, division, unicode_literals,
                        absolute_import)
from builtins import range, open

import os
import sys
from copy import deepcopy
import pytest

from ... import engine as pe
from ....interfaces import base as nib
from ....interfaces import utility as niu
from .... import config
from ..utils import clean_working_directory, write_workflow_prov


class InputSpec(nib.TraitedSpec):
    in_file = nib.File(exists=True, copyfile=True)


class OutputSpec(nib.TraitedSpec):
    output1 = nib.traits.List(nib.traits.Int, desc='outputs')


class UtilsTestInterface(nib.BaseInterface):
    input_spec = InputSpec
    output_spec = OutputSpec

    def _run_interface(self, runtime):
        runtime.returncode = 0
        return runtime

    def _list_outputs(self):
        outputs = self._outputs().get()
        outputs['output1'] = [1]
        return outputs


def test_identitynode_removal(tmpdir):
    def test_function(arg1, arg2, arg3):
        import numpy as np
        return (np.array(arg1) + arg2 + arg3).tolist()

    wf = pe.Workflow(name="testidentity", base_dir=tmpdir.strpath)

    n1 = pe.Node(
        niu.IdentityInterface(fields=['a', 'b']),
        name='src',
        base_dir=tmpdir.strpath)
    n1.iterables = ('b', [0, 1, 2, 3])
    n1.inputs.a = [0, 1, 2, 3]

    n2 = pe.Node(niu.Select(), name='selector', base_dir=tmpdir.strpath)
    wf.connect(n1, ('a', test_function, 1, -1), n2, 'inlist')
    wf.connect(n1, 'b', n2, 'index')

    n3 = pe.Node(
        niu.IdentityInterface(fields=['c', 'd']),
        name='passer',
        base_dir=tmpdir.strpath)
    n3.inputs.c = [1, 2, 3, 4]
    wf.connect(n2, 'out', n3, 'd')

    n4 = pe.Node(niu.Select(), name='selector2', base_dir=tmpdir.strpath)
    wf.connect(n3, ('c', test_function, 1, -1), n4, 'inlist')
    wf.connect(n3, 'd', n4, 'index')

    fg = wf._create_flat_graph()
    wf._set_needed_outputs(fg)
    eg = pe.generate_expanded_graph(deepcopy(fg))
    assert len(eg.nodes()) == 8


def test_clean_working_directory(tmpdir):
    class OutputSpec(nib.TraitedSpec):
        files = nib.traits.List(nib.File)
        others = nib.File()

    class InputSpec(nib.TraitedSpec):
        infile = nib.File()

    outputs = OutputSpec()
    inputs = InputSpec()

    filenames = [
        'file.hdr', 'file.img', 'file.BRIK', 'file.HEAD', '_0x1234.json',
        'foo.txt'
    ]
    outfiles = []
    for filename in filenames:
        outfile = tmpdir.join(filename)
        outfile.write('dummy')
        outfiles.append(outfile.strpath)
    outputs.files = outfiles[:4:2]
    outputs.others = outfiles[5]
    inputs.infile = outfiles[-1]
    needed_outputs = ['files']
    config.set_default_config()
    assert os.path.exists(outfiles[5])
    config.set_default_config()
    config.set('execution', 'remove_unnecessary_outputs', False)
    out = clean_working_directory(outputs, tmpdir.strpath, inputs,
                                  needed_outputs, deepcopy(config._sections))
    assert os.path.exists(outfiles[5])
    assert out.others == outfiles[5]
    config.set('execution', 'remove_unnecessary_outputs', True)
    out = clean_working_directory(outputs, tmpdir.strpath, inputs,
                                  needed_outputs, deepcopy(config._sections))
    assert os.path.exists(outfiles[1])
    assert os.path.exists(outfiles[3])
    assert os.path.exists(outfiles[4])
    assert not os.path.exists(outfiles[5])
    assert out.others == nib.Undefined
    assert len(out.files) == 2
    config.set_default_config()


def create_wf(name):
    """Creates a workflow for the following tests"""
    def fwhm(fwhm):
        return fwhm

    pipe = pe.Workflow(name=name)
    process = pe.Node(
        niu.Function(
            input_names=['fwhm'], output_names=['fwhm'], function=fwhm),
        name='proc')
    process.iterables = ('fwhm', [0])
    process2 = pe.Node(
        niu.Function(
            input_names=['fwhm'], output_names=['fwhm'], function=fwhm),
        name='proc2')
    process2.iterables = ('fwhm', [0])
    pipe.connect(process, 'fwhm', process2, 'fwhm')
    return pipe


def test_multi_disconnected_iterable(tmpdir):
    metawf = pe.Workflow(name='meta')
    metawf.base_dir = tmpdir.strpath
    metawf.add_nodes([create_wf('wf%d' % i) for i in range(30)])
    eg = metawf.run(plugin='Linear')
    assert len(eg.nodes()) == 60


def test_provenance(tmpdir):
    metawf = pe.Workflow(name='meta')
    metawf.base_dir = tmpdir.strpath
    metawf.add_nodes([create_wf('wf%d' % i) for i in range(1)])
    eg = metawf.run(plugin='Linear')
    prov_base = tmpdir.join('workflow_provenance_test').strpath
    psg = write_workflow_prov(eg, prov_base, format='all')
    assert len(psg.bundles) == 2
    assert len(psg.get_records()) == 7
