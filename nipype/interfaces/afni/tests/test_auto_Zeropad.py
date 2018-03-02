# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import Zeropad


def test_Zeropad_inputs():
    input_map = dict(
        A=dict(
            argstr='-A %i',
            xor=['master'],
        ),
        AP=dict(
            argstr='-AP %i',
            xor=['master'],
        ),
        I=dict(
            argstr='-I %i',
            xor=['master'],
        ),
        IS=dict(
            argstr='-IS %i',
            xor=['master'],
        ),
        L=dict(
            argstr='-L %i',
            xor=['master'],
        ),
        P=dict(
            argstr='-P %i',
            xor=['master'],
        ),
        R=dict(
            argstr='-R %i',
            xor=['master'],
        ),
        RL=dict(
            argstr='-RL %i',
            xor=['master'],
        ),
        S=dict(
            argstr='-S %i',
            xor=['master'],
        ),
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
        in_files=dict(
            argstr='%s',
            copyfile=False,
            mandatory=True,
            position=-1,
        ),
        master=dict(
            argstr='-master %s',
            xor=['I', 'S', 'A', 'P', 'L', 'R', 'z', 'RL', 'AP', 'IS', 'mm'],
        ),
        mm=dict(
            argstr='-mm',
            xor=['master'],
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr='-prefix %s',
            name_template='zeropad',
        ),
        outputtype=dict(),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        z=dict(
            argstr='-z %i',
            xor=['master'],
        ),
    )
    inputs = Zeropad.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Zeropad_outputs():
    output_map = dict(out_file=dict(), )
    outputs = Zeropad.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
