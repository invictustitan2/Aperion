# Stubs for difflib

# Based on https://docs.python.org/3.2/library/difflib.html

from typing import (
    Callable,
    Generic,
    Iterable,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
)

_T = TypeVar("_T")

class SequenceMatcher(Generic[_T]):
    def __init__(
        self,
        isjunk: Optional[Callable[[_T], bool]] = ...,
        a: Sequence[_T] = ...,
        b: Sequence[_T] = ...,
        autojunk: bool = ...,
    ) -> None: ...
    def set_seqs(self, a: Sequence[_T], b: Sequence[_T]) -> None: ...
    def set_seq1(self, a: Sequence[_T]) -> None: ...
    def set_seq2(self, b: Sequence[_T]) -> None: ...
    def find_longest_match(
        self, alo: int, ahi: int, blo: int, bhi: int
    ) -> Tuple[int, int, int]: ...
    def get_matching_blocks(self) -> List[Tuple[int, int, int]]: ...
    def get_opcodes(self) -> List[Tuple[str, int, int, int, int]]: ...
    def get_grouped_opcodes(
        self, n: int = ...
    ) -> Iterable[Tuple[str, int, int, int, int]]: ...
    def ratio(self) -> float: ...
    def quick_ratio(self) -> float: ...
    def real_quick_ratio(self) -> float: ...

def get_close_matches(
    word: Sequence[_T],
    possibilities: List[Sequence[_T]],
    n: int = ...,
    cutoff: float = ...,
) -> List[Sequence[_T]]: ...

class Differ:
    def __init__(
        self,
        linejunk: Callable[[str], bool] = ...,
        charjunk: Callable[[str], bool] = ...,
    ) -> None: ...
    def compare(self, a: Sequence[str], b: Sequence[str]) -> Iterator[str]: ...

def IS_LINE_JUNK(str) -> bool: ...
def IS_CHARACTER_JUNK(str) -> bool: ...
def unified_diff(
    a: Sequence[str],
    b: Sequence[str],
    fromfile: str = ...,
    tofile: str = ...,
    fromfiledate: str = ...,
    tofiledate: str = ...,
    n: int = ...,
    lineterm: str = ...,
) -> Iterator[str]: ...
def context_diff(
    a: Sequence[str],
    b: Sequence[str],
    fromfile: str = ...,
    tofile: str = ...,
    fromfiledate: str = ...,
    tofiledate: str = ...,
    n: int = ...,
    lineterm: str = ...,
) -> Iterator[str]: ...
def ndiff(
    a: Sequence[str],
    b: Sequence[str],
    linejunk: Callable[[str], bool] = ...,
    charjunk: Callable[[str], bool] = ...,
) -> Iterator[str]: ...

class HtmlDiff(object):
    def __init__(
        self,
        tabsize: int = ...,
        wrapcolumn: int = ...,
        linejunk: Callable[[str], bool] = ...,
        charjunk: Callable[[str], bool] = ...,
    ) -> None: ...
    def make_file(
        self,
        fromlines: Sequence[str],
        tolines: Sequence[str],
        fromdesc: str = ...,
        todesc: str = ...,
        context: bool = ...,
        numlines: int = ...,
    ) -> str: ...
    def make_table(
        self,
        fromlines: Sequence[str],
        tolines: Sequence[str],
        fromdesc: str = ...,
        todesc: str = ...,
        context: bool = ...,
        numlines: int = ...,
    ) -> str: ...

def restore(delta: Iterable[str], which: int) -> Iterator[int]: ...
