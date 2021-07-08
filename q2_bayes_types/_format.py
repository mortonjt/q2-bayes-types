import qiime2.plugin.model as model
from qiime2.plugin import ValidationError
import qiime2
import arviz as az


class MonteCarloTensorFormat(model.BinaryFileFormat):

    def sniff(self):
        try:
            az.InferenceData.from_netcdf(str(self))
            return True
        except Exception:
            return False


MonteCarloTensorDirectoryFormat = model.SingleFileDirectoryFormat(
    'MonteCarloTensorDirectoryFormat', 'monte-carlo-samples.az',
    MonteCarloTensorFormat)


plugin.register_formats(
    DifferentialFormat, DifferentialDirectoryFormat
)
