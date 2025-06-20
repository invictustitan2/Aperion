# ModuleSpec, ModuleType, Loader are part of a dependency cycle.
# They are officially defined/exported in other places:
#
# - ModuleType in types
# - Loader in importlib.abc
# - ModuleSpec in importlib.machinery (3.4 and later only)

import sys
from abc import ABCMeta
from typing import Any, Optional

if sys.version_info >= (3, 4):
    class ModuleSpec:
        def __init__(
            self,
            name: str,
            loader: Optional["Loader"],
            *,
            origin: str = None,
            loader_state: Any = None,
            is_package: bool = None
        ) -> None: ...
        name = ...  # type: str
        loader = ...  # type: Optional[Loader]
        origin = ...  # type: Optional[str]
        submodule_search_locations = ...  # type: Optional[List[str]]
        loader_state = ...  # type: Any
        cached = ...  # type: Optional[str]
        parent = ...  # type: Optional[str]
        has_location = ...  # type: bool

class ModuleType:
    __name__ = ...  # type: str
    __file__ = ...  # type: str
    if sys.version_info >= (3, 4):
        __loader__ = ...  # type: Optional[Loader]
        __package__ = ...  # type: Optional[str]
        __spec__ = ...  # type: Optional[ModuleSpec]

    def __init__(self, name: str, doc: str) -> None: ...

class Loader(metaclass=ABCMeta):
    def load_module(self, fullname: str) -> ModuleType: ...
    if sys.version_info >= (3, 3):
        def module_repr(self, module: ModuleType) -> str: ...
    if sys.version_info >= (3, 4):
        def create_module(self, spec: ModuleSpec) -> Optional[ModuleType]: ...
        # Not defined on the actual class for backwards-compatibility reasons,
        # but expected in new code.
        def exec_module(self, module: ModuleType) -> None: ...
