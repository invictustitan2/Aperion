from typing import Any, Callable, Iterable, Optional, TypeVar

from ._base import Executor, Future

EXTRA_QUEUED_CALLS = ...  # type: Any

class BrokenProcessPool(RuntimeError): ...

_T = TypeVar("_T")

class ProcessPoolExecutor(Executor):
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
