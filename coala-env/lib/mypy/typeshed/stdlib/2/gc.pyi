# Stubs for gc

from typing import Any, List, Tuple

def enable() -> None: ...
def disable() -> None: ...
def isenabled() -> bool: ...
def collect(generation: int = ...) -> int: ...
def set_debug(flags: int) -> None: ...
def get_debug() -> int: ...
def get_objects() -> List[Any]: ...
def set_threshold(
    threshold0: int, threshold1: int = ..., threshold2: int = ...
) -> None: ...
def get_count() -> Tuple[int, int, int]: ...
def get_threshold() -> Tuple[int, int, int]: ...
def get_referrers(*objs: Any) -> List[Any]: ...
def get_referents(*objs: Any) -> List[Any]: ...
def is_tracked(obj: Any) -> bool: ...

garbage = ...  # type: List[Any]

DEBUG_STATS = ...  # type: int
DEBUG_COLLECTABLE = ...  # type: int
DEBUG_UNCOLLECTABLE = ...  # type: int
DEBUG_INSTANCES = ...  # type: int
DEBUG_OBJECTS = ...  # type: int
DEBUG_SAVEALL = ...  # type: int
DEBUG_LEAK = ...  # type: int
