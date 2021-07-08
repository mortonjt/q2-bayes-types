import biom
import skbio
import qiime2

import arviz as az

from . import  MonteCarloTensorFormat,


@plugin.register_transformer
def _225(ff: MonteCarloTensorFormat) -> az.InferenceData:
    return az.InferenceData.from_netcdf(str(ff))


@plugin.register_transformer
def _226(obj: az.InferenceData) -> MonteCarloTensorFormat:
    ff = MonteCarloTensorFormat()
    obj.to_netcdf(str(ff))
    return ff
