from qiime2.plugin import SemanticType
from ..plugin_setup import plugin
from . import MonteCarloTensorDirectoryFormat


MonteCarloTensor = SemanticType('MonteCarloTensor')


plugin.register_semantic_types(MonteCarloTensor)
plugin.register_semantic_type_to_format(
    MonteCarloTensor, MonteCarloTensorDirectoryFormat)
