# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import TCorrMap


def test_TCorrMap_inputs():
    input_map = dict(
        absolute_threshold=dict(
            argstr='-Thresh %f %s',
            name_source='in_file',
            suffix='_thresh',
            xor=('absolute_threshold', 'var_absolute_threshold',
                 'var_absolute_threshold_normalize'),
        ),
        args=dict(argstr='%s', ),
        automask=dict(argstr='-automask', ),
        average_expr=dict(
            argstr='-Aexpr %s %s',
            name_source='in_file',
            suffix='_aexpr',
            xor=('average_expr', 'average_expr_nonzero', 'sum_expr'),
        ),
        average_expr_nonzero=dict(
            argstr='-Cexpr %s %s',
            name_source='in_file',
            suffix='_cexpr',
            xor=('average_expr', 'average_expr_nonzero', 'sum_expr'),
        ),
        bandpass=dict(argstr='-bpass %f %f', ),
        blur_fwhm=dict(argstr='-Gblur %f', ),
        correlation_maps=dict(
            argstr='-CorrMap %s',
            name_source='in_file',
        ),
        correlation_maps_masked=dict(
            argstr='-CorrMask %s',
            name_source='in_file',
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        expr=dict(),
        histogram=dict(
            argstr='-Hist %d %s',
            name_source='in_file',
            suffix='_hist',
        ),
        histogram_bin_numbers=dict(),
        in_file=dict(
            argstr='-input %s',
            copyfile=False,
            mandatory=True,
        ),
        mask=dict(argstr='-mask %s', ),
        mean_file=dict(
            argstr='-Mean %s',
            name_source='in_file',
            suffix='_mean',
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr='-prefix %s',
            name_source=['in_file'],
            name_template='%s_afni',
        ),
        outputtype=dict(),
        pmean=dict(
            argstr='-Pmean %s',
            name_source='in_file',
            suffix='_pmean',
        ),
        polort=dict(argstr='-polort %d', ),
        qmean=dict(
            argstr='-Qmean %s',
            name_source='in_file',
            suffix='_qmean',
        ),
        regress_out_timeseries=dict(argstr='-ort %s', ),
        seeds=dict(
            argstr='-seed %s',
            xor='seeds_width',
        ),
        seeds_width=dict(
            argstr='-Mseed %f',
            xor='seeds',
        ),
        sum_expr=dict(
            argstr='-Sexpr %s %s',
            name_source='in_file',
            suffix='_sexpr',
            xor=('average_expr', 'average_expr_nonzero', 'sum_expr'),
        ),
        thresholds=dict(),
        var_absolute_threshold=dict(
            argstr='-VarThresh %f %f %f %s',
            name_source='in_file',
            suffix='_varthresh',
            xor=('absolute_threshold', 'var_absolute_threshold',
                 'var_absolute_threshold_normalize'),
        ),
        var_absolute_threshold_normalize=dict(
            argstr='-VarThreshN %f %f %f %s',
            name_source='in_file',
            suffix='_varthreshn',
            xor=('absolute_threshold', 'var_absolute_threshold',
                 'var_absolute_threshold_normalize'),
        ),
        zmean=dict(
            argstr='-Zmean %s',
            name_source='in_file',
            suffix='_zmean',
        ),
    )
    inputs = TCorrMap.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_TCorrMap_outputs():
    output_map = dict(
        absolute_threshold=dict(),
        average_expr=dict(),
        average_expr_nonzero=dict(),
        correlation_maps=dict(),
        correlation_maps_masked=dict(),
        histogram=dict(),
        mean_file=dict(),
        pmean=dict(),
        qmean=dict(),
        sum_expr=dict(),
        var_absolute_threshold=dict(),
        var_absolute_threshold_normalize=dict(),
        zmean=dict(),
    )
    outputs = TCorrMap.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
