# Stubs for queue

# NOTE: These are incomplete!

from typing import Generic, Optional, TypeVar

_T = TypeVar("_T")

class Empty(Exception): ...
class Full(Exception): ...

class Queue(Generic[_T]):
    def __init__(self, maxsize: int = ...) -> None: ...
    def full(self) -> bool: ...
    def get(self, block: bool = ..., timeout: Optional[float] = ...) -> _T: ...
    def get_nowait(self) -> _T: ...
    def put(
        self, item: _T, block: bool = ..., timeout: Optional[float] = ...
    ) -> None: ...
    def put_nowait(self, item: _T) -> None: ...
    def join(self) -> None: ...
    def qsize(self) -> int: ...
    def task_done(self) -> None:
        pass

class PriorityQueue(Queue): ...
class LifoQueue(Queue): ...
