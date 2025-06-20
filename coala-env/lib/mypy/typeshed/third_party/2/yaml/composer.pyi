# Stubs for yaml.composer (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from yaml.error import MarkedYAMLError

class ComposerError(MarkedYAMLError): ...

class Composer:
    anchors = ...  # type: Any
    def __init__(self) -> None: ...
    def check_node(self): ...
    def get_node(self): ...
    def get_single_node(self): ...
    def compose_document(self): ...
    def compose_node(self, parent, index): ...
    def compose_scalar_node(self, anchor): ...
    def compose_sequence_node(self, anchor): ...
    def compose_mapping_node(self, anchor): ...
