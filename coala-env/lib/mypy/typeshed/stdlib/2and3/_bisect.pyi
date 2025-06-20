"""Stub file for the '_bisect' module."""

from typing import Sequence, TypeVar

T = TypeVar("T")

def bisect(a: Sequence[T], x: T, lo: int = ..., hi: int = ...) -> int: ...
def bisect_left(a: Sequence[T], x: T, lo: int = ..., hi: int = ...) -> int: ...
def bisect_right(a: Sequence[T], x: T, lo: int = ..., hi: int = ...) -> int: ...
def insort(a: Sequence[T], x: T, lo: int = ..., hi: int = ...) -> None: ...
def insort_left(a: Sequence[T], x: T, lo: int = ..., hi: int = ...) -> None: ...
def insort_right(a: Sequence[T], x: T, lo: int = ..., hi: int = ...) -> None: ...
