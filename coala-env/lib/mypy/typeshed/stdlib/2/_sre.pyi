"""Stub file for the '_sre' module."""

from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
    overload,
)

CODESIZE = ...  # type: int
MAGIC = ...  # type: int
MAXREPEAT = ...  # type: long
copyright = ...  # type: str

class SRE_Match(object):
    def start(self, group: int = ...) -> int:
        raise IndexError()

    def end(self, group: int = ...) -> int:
        raise IndexError()

    def expand(self, s: str) -> Any: ...
    @overload
    def group(self) -> str: ...
    @overload
    def group(self, group: int = ...) -> Optional[str]: ...
    def groupdict(self) -> Dict[int, Optional[str]]: ...
    def groups(self) -> Tuple[Optional[str]]: ...
    def span(self) -> Tuple[int, int]:
        raise IndexError()

class SRE_Scanner(object):
    pattern = ...  # type: str
    def match(self) -> SRE_Match: ...
    def search(self) -> SRE_Match: ...

class SRE_Pattern(object):
    pattern = ...  # type: str
    flags = ...  # type: int
    groups = ...  # type: int
    groupindex = ...  # type: Mapping[int, int]
    indexgroup = ...  # type: Sequence[int]
    def findall(
        self, source: str, pos: int = ..., endpos: int = ...
    ) -> List[Union[tuple, str]]: ...
    def finditer(
        self, source: str, pos: int = ..., endpos: int = ...
    ) -> Iterable[Union[tuple, str]]: ...
    def match(self, pattern, pos: int = ..., endpos: int = ...) -> SRE_Match: ...
    def scanner(self, s: str, start: int = ..., end: int = ...) -> SRE_Scanner: ...
    def search(self, pattern, pos: int = ..., endpos: int = ...) -> SRE_Match: ...
    def split(self, source: str, maxsplit: int = ...) -> List[Optional[str]]: ...
    def sub(self, repl: str, string: str, count: int = ...) -> tuple: ...
    def subn(self, repl: str, string: str, count: int = ...) -> tuple: ...

def compile(
    pattern: str,
    flags: int,
    code: List[int],
    groups: int = ...,
    groupindex: Mapping[int, int] = ...,
    indexgroup: Sequence[int] = ...,
) -> SRE_Pattern:
    raise OverflowError()

def getcodesize() -> int: ...
def getlower(a: int, b: int) -> int: ...
