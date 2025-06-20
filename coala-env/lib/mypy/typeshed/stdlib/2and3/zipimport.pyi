"""Stub file for the 'zipimport' module."""

from types import CodeType, ModuleType
from typing import Optional

class ZipImportError(ImportError): ...

class zipimporter(object):
    archive = ...  # type: str
    prefix = ...  # type: str
    def __init__(self, archivepath: str) -> None: ...
    def find_module(self, fullname: str, path: str = ...) -> Optional[zipimporter]: ...
    def get_code(self, fullname: str) -> CodeType: ...
    def get_data(self, pathname: str) -> str: ...
    def get_filename(self, fullname: str) -> str: ...
    def get_source(self, fullname: str) -> Optional[str]: ...
    def is_package(self, fullname: str) -> bool: ...
    def load_module(self, fullname: str) -> ModuleType: ...
