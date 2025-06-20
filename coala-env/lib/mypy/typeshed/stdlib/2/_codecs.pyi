"""Stub file for the '_codecs' module."""

import codecs
from typing import Any, AnyStr, Callable, Optional, Tuple

# For convenience:
_Handler = Callable[[Exception], Tuple[unicode, int]]

# Not exposed. In Python 2, this is defined in unicode.c:
class _EncodingMap(object):
    def size(self) -> int: ...

def register(search_function: Callable[[str], Any]) -> None: ...
def register_error(errors: str, handler: _Handler) -> None: ...
def lookup(a: str) -> codecs.CodecInfo: ...
def lookup_error(a: str) -> _Handler: ...
def decode(obj: Any, encoding: str = ..., errors: str = ...) -> Any: ...
def encode(obj: Any, encoding: str = ..., errors: str = ...) -> Any: ...
def charmap_build(a: unicode) -> _EncodingMap: ...
def ascii_decode(data: AnyStr, errors: str = ...) -> Tuple[unicode, int]: ...
def ascii_encode(data: AnyStr, errors: str = ...) -> Tuple[str, int]: ...
def charbuffer_encode(data: AnyStr, errors: str = ...) -> Tuple[str, int]: ...
def charmap_decode(
    data: AnyStr, errors: str = ..., mapping: Optional[_EncodingMap] = ...
) -> Tuple[unicode, int]: ...
def charmap_encode(
    data: AnyStr, errors: str, mapping: Optional[_EncodingMap] = ...
) -> Tuple[str, int]: ...
def escape_decode(data: AnyStr, errors: str = ...) -> Tuple[unicode, int]: ...
def escape_encode(data: AnyStr, errors: str = ...) -> Tuple[str, int]: ...
def latin_1_decode(data: AnyStr, errors: str = ...) -> Tuple[unicode, int]: ...
def latin_1_encode(data: AnyStr, errors: str = ...) -> Tuple[str, int]: ...
def raw_unicode_escape_decode(
    data: AnyStr, errors: str = ...
) -> Tuple[unicode, int]: ...
def raw_unicode_escape_encode(data: AnyStr, errors: str = ...) -> Tuple[str, int]: ...
def readbuffer_encode(data: AnyStr, errors: str = ...) -> Tuple[str, int]: ...
def unicode_escape_decode(data: AnyStr, errors: str = ...) -> Tuple[unicode, int]: ...
def unicode_escape_encode(data: AnyStr, errors: str = ...) -> Tuple[str, int]: ...
def unicode_internal_decode(data: AnyStr, errors: str = ...) -> Tuple[unicode, int]: ...
def unicode_internal_encode(data: AnyStr, errors: str = ...) -> Tuple[str, int]: ...
def utf_16_be_decode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[unicode, int]: ...
def utf_16_be_encode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[str, int]: ...
def utf_16_decode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[unicode, int]: ...
def utf_16_encode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[str, int]: ...
def utf_16_ex_decode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[unicode, int]: ...
def utf_16_le_decode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[unicode, int]: ...
def utf_16_le_encode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[str, int]: ...
def utf_32_be_decode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[unicode, int]: ...
def utf_32_be_encode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[str, int]: ...
def utf_32_decode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[unicode, int]: ...
def utf_32_encode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[str, int]: ...
def utf_32_ex_decode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[unicode, int]: ...
def utf_32_le_decode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[unicode, int]: ...
def utf_32_le_encode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[str, int]: ...
def utf_7_decode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[unicode, int]: ...
def utf_7_encode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[str, int]: ...
def utf_8_decode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[unicode, int]: ...
def utf_8_encode(
    data: AnyStr, errors: str = ..., final: int = ...
) -> Tuple[str, int]: ...
