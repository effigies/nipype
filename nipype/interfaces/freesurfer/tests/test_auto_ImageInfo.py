# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import ImageInfo


def test_ImageInfo_inputs():
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
        in_file=dict(
            argstr='%s',
            position=1,
        ),
        subjects_dir=dict(),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = ImageInfo.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ImageInfo_outputs():
    output_map = dict(
        TE=dict(),
        TI=dict(),
        TR=dict(),
        data_type=dict(),
        dimensions=dict(),
        file_format=dict(),
        info=dict(),
        orientation=dict(),
        out_file=dict(),
        ph_enc_dir=dict(),
        vox_sizes=dict(),
    )
    outputs = ImageInfo.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
