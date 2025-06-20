# Stubs for xml.etree.ElementPath (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Callable, Dict, Generator, List, Optional, Tuple, TypeVar, Union

from .ElementTree import Element

xpath_tokenizer_re = ...  # type: Pattern

_token = Tuple[str, str]
_next = Callable[[], _token]
_callback = Callable[
    ["_SelectorContext", List[Element]], Generator[Element, None, None]
]

def xpath_tokenizer(
    pattern: str, namespaces: Dict[str, str] = ...
) -> Generator[_token, None, None]: ...
def get_parent_map(context: "_SelectorContext") -> Dict[Element, Element]: ...
def prepare_child(next: _next, token: _token) -> _callback: ...
def prepare_star(next: _next, token: _token) -> _callback: ...
def prepare_self(next: _next, token: _token) -> _callback: ...
def prepare_descendant(next: _next, token: _token) -> _callback: ...
def prepare_parent(next: _next, token: _token) -> _callback: ...
def prepare_predicate(next: _next, token: _token) -> _callback: ...

ops = ...  # type: Dict[str, Callable[[_next, _token], _callback]]

class _SelectorContext:
    parent_map = ...  # type: Dict[Element, Element]
    root = ...  # type: Element
    def __init__(self, root: Element) -> None: ...

_T = TypeVar("_T")

def iterfind(
    elem: Element, path: str, namespaces: Dict[str, str] = ...
) -> List[Element]: ...
def find(
    elem: Element, path: str, namespaces: Dict[str, str] = ...
) -> Optional[Element]: ...
def findall(
    elem: Element, path: str, namespaces: Dict[str, str] = ...
) -> List[Element]: ...
def findtext(
    elem: Element, path: str, default: _T = ..., namespaces: Dict[str, str] = ...
) -> Union[_T, str]: ...
