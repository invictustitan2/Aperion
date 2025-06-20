# Stubs for mmap

import sys
from typing import (
    Container,
    Generic,
    Iterable,
    Optional,
    Reversible,
    Sequence,
    Sized,
    TypeVar,
    Union,
    overload,
)

_T = TypeVar("_T", str, bytes)

from types import TracebackType

# TODO already in PEP, have to get added to mypy
from typing import Type

_C = TypeVar("_C")

class _ContextManager(Generic[_C]):
    def __enter__(self) -> _C: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[Exception],
        exc_tb: Optional[TracebackType],
    ) -> bool: ...

ACCESS_READ = ...  # type: int
ACCESS_WRITE = ...  # type: int
ACCESS_COPY = ...  # type: int

ALLOCATIONGRANULARITY = ...  # type: int

if sys.platform != "win32":
    MAP_PRIVATE = ...  # type: int
    MAP_SHARED = ...  # type: int
    PROT_READ = ...  # type: int
    PROT_WRITE = ...  # type: int

    PAGESIZE = ...  # type: int

class _mmap(Generic[_T]):
    if sys.platform == "win32":
        def __init__(
            self,
            fileno: int,
            length: int,
            tagname: Optional[str] = ...,
            access: int = ...,
            offset: int = ...,
        ) -> None: ...
    else:
        def __init__(
            self,
            fileno: int,
            length: int,
            flags: int = ...,
            prot: int = ...,
            access: int = ...,
            offset: int = ...,
        ) -> None: ...

    def close(self) -> None: ...
    def find(self, sub: _T, start: int = ..., end: int = ...) -> int: ...
    def flush(self, offset: int = ..., size: int = ...) -> int: ...
    def move(self, dest: int, src: int, count: int) -> None: ...
    def read(self, n: int = ...) -> _T: ...
    def read_byte(self) -> _T: ...
    def readline(self) -> _T: ...
    def resize(self, newsize: int) -> None: ...
    def seek(self, pos: int, whence: int = ...) -> None: ...
    def size(self) -> int: ...
    def tell(self) -> int: ...
    def write(self, bytes: _T) -> None: ...
    def write_byte(self, byte: _T) -> None: ...
    def __len__(self) -> int: ...

if sys.version_info >= (3,):
    class mmap(
        _mmap,
        _ContextManager[mmap],
        Iterable[bytes],
        Container[bytes],
        Sized,
        Reversible[bytes],
    ):
        closed = ...  # type: bool
        def rfind(self, sub: bytes, start: int = ..., stop: int = ...) -> int: ...
        @overload
        def __getitem__(self, index: int) -> int: ...
        @overload
        def __getitem__(self, index: slice) -> bytes: ...
        def __delitem__(self, index: Union[int, slice]) -> None: ...
        @overload
        def __setitem__(self, index: int, object: int) -> None: ...
        @overload
        def __setitem__(self, index: slice, object: bytes) -> None: ...

else:
    class mmap(_mmap, Sequence[bytes]):
        def rfind(self, string: bytes, start: int = ..., stop: int = ...) -> int: ...
        def __getitem__(self, index: Union[int, slice]) -> bytes: ...
        def __delitem__(self, index: Union[int, slice]) -> None: ...
        def __setitem__(self, index: Union[int, slice], object: bytes) -> None: ...
