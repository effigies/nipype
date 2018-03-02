# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..maxcurvature import maxcurvature


def test_maxcurvature_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        image=dict(argstr='--image %s', ),
        output=dict(
            argstr='--output %s',
            hash_files=False,
        ),
        sigma=dict(argstr='--sigma %f', ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        verbose=dict(argstr='--verbose ', ),
    )
    inputs = maxcurvature.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_maxcurvature_outputs():
    output_map = dict(output=dict(), )
    outputs = maxcurvature.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
