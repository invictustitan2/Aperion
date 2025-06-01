# Stubs for sqlalchemy.util.compat (Python 2)

from collections import namedtuple

# import configparser

py33 = ... # type: Any
py32 = ... # type: Any
py3k = ... # type: Any
py2k = ... # type: Any
py265 = ... # type: Any
jython = ... # type: Any
pypy = ... # type: Any
win32 = ... # type: Any
cpython = ... # type: Any
next = ... # type: Any
safe_kwarg = ... # type: Any

ArgSpec = namedtuple('ArgSpec', ['args', 'varargs', 'keywords', 'defaults'])

def inspect_getargspec(func): ...

string_types = ... # type: Any
binary_type = ... # type: Any
text_type = unicode
int_types = ... # type: Any

def callable(fn): ...
def cmp(a, b): ...

itertools_filterfalse = ... # type: Any
itertools_filter = ... # type: Any
itertools_imap = ... # type: Any

def b64encode(x): ...
def b64decode(x): ...

def iterbytes(buf): ...
def u(s): ...
def ue(s): ...
def b(s): ...
def import_(*args): ...

reduce = ... # type: Any

def print_(*args, **kwargs): ...

time_func = ... # type: Any

def reraise(tp, value, tb=..., cause=...): ...
def raise_from_cause(exception, exc_info=...): ...

def exec_(func_text, globals_, lcl=...): ...
def with_metaclass(meta, *bases): ...
def nested(*managers): ...
