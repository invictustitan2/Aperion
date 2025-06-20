from typing import Any, Callable, Iterable, Optional, TypeVar

from ._base import Executor, Future

_T = TypeVar("_T")

class ThreadPoolExecutor(Executor):
    def __init__(self, max_workers: Optional[int] = ...) -> None: ...
    def submit(
        self, fn: Callable[..., _T], *args: Any, **kwargs: Any
    ) -> Future[_T]: ...
    def map(
        self,
        func: Callable[..., _T],
        *iterables: Any,
        timeout: Optional[float] = ...,
        chunksize: int = ...
    ) -> Iterable[_T]: ...
    def shutdown(self, wait: bool = ...) -> None: ...
