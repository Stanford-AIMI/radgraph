"""
Coreference resolution is defined as follows: given a document, find and cluster entity mentions.
"""

from radgraph.allennlp_models.coref.dataset_readers.conll import ConllCorefReader
from radgraph.allennlp_models.coref.dataset_readers.preco import PrecoReader
from radgraph.allennlp_models.coref.dataset_readers.winobias import WinobiasReader
from radgraph.allennlp_models.coref.models.coref import CoreferenceResolver
