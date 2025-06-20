# Stubs for shutil
import sys
from typing import IO, Any, AnyStr, Callable, Iterable, List, Sequence, Tuple

# Based on http://docs.python.org/3.2/library/shutil.html

# 'bytes' paths are not properly supported: they don't work with all functions,
# sometimes they only work partially (broken exception messages), and the test
# cases don't use them.

def copyfileobj(fsrc: IO[AnyStr], fdst: IO[AnyStr], length: int = ...) -> None: ...
def copyfile(src: str, dst: str) -> None: ...
def copymode(src: str, dst: str) -> None: ...
def copystat(src: str, dst: str) -> None: ...
def copy(src: str, dst: str) -> None: ...
def copy2(src: str, dst: str) -> None: ...
def ignore_patterns(*patterns: str) -> Callable[[str, List[str]], Iterable[str]]: ...
def copytree(
    src: str,
    dst: str,
    symlinks: bool = ...,
    ignore: Callable[[str, List[str]], Iterable[str]] = ...,
    copy_function: Callable[[str, str], None] = ...,
    ignore_dangling_symlinks: bool = ...,
) -> None: ...
def rmtree(
    path: str, ignore_errors: bool = ..., onerror: Callable[[Any, str, Any], None] = ...
) -> None: ...
def move(src: str, dst: str) -> None: ...

class Error(Exception): ...

if sys.version_info >= (3, 4):
    class SameFileError(Error): ...

def make_archive(
    base_name: str,
    format: str,
    root_dir: str = ...,
    base_dir: str = ...,
    verbose: bool = ...,
    dry_run: bool = ...,
    owner: str = ...,
    group: str = ...,
    logger: Any = ...,
) -> str: ...
def get_archive_formats() -> List[Tuple[str, str]]: ...
def register_archive_format(
    name: str,
    function: Any,
    extra_args: Sequence[Tuple[str, Any]] = ...,
    description: str = ...,
) -> None: ...
def unregister_archive_format(name: str) -> None: ...
def unpack_archive(
    filename: str, extract_dir: str = ..., format: str = ...
) -> None: ...
def register_unpack_format(
    name: str,
    extensions: List[str],
    function: Any,
    extra_args: Sequence[Tuple[str, Any]] = ...,
    description: str = ...,
) -> None: ...
def unregister_unpack_format(name: str) -> None: ...
def get_unpack_formats() -> List[Tuple[str, List[str], str]]: ...
def which(cmd: str, mode: int = ..., path: str = ...): ...
