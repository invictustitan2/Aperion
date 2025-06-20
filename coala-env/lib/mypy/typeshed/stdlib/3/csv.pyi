# Stubs for csv (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Iterable

QUOTE_ALL = ...  # type: int
QUOTE_MINIMAL = ...  # type: int
QUOTE_NONE = ...  # type: int
QUOTE_NONNUMERIC = ...  # type: int

class Error(Exception): ...

def writer(csvfile, dialect=..., **fmtparams): ...
def reader(csvfile, dialect=..., **fmtparams): ...
def register_dialect(name, dialect=..., **fmtparams): ...
def unregister_dialect(name): ...
def get_dialect(name): ...
def list_dialects(): ...
def field_size_limit(new_limit=...): ...

class Dialect:
    delimiter = ...  # type: Any
    quotechar = ...  # type: Any
    escapechar = ...  # type: Any
    doublequote = ...  # type: Any
    skipinitialspace = ...  # type: Any
    lineterminator = ...  # type: Any
    quoting = ...  # type: Any
    def __init__(self) -> None: ...

class excel(Dialect):
    delimiter = ...  # type: Any
    quotechar = ...  # type: Any
    doublequote = ...  # type: Any
    skipinitialspace = ...  # type: Any
    lineterminator = ...  # type: Any
    quoting = ...  # type: Any

class excel_tab(excel):
    delimiter = ...  # type: Any

class unix_dialect(Dialect):
    delimiter = ...  # type: Any
    quotechar = ...  # type: Any
    doublequote = ...  # type: Any
    skipinitialspace = ...  # type: Any
    lineterminator = ...  # type: Any
    quoting = ...  # type: Any

class DictReader(Iterable):
    restkey = ...  # type: Any
    restval = ...  # type: Any
    reader = ...  # type: Any
    dialect = ...  # type: Any
    line_num = ...  # type: Any
    fieldnames = ...  # type: Any # Actually a property
    def __init__(
        self, f, fieldnames=..., restkey=..., restval=..., dialect=..., *args, **kwds
    ): ...
    def __iter__(self): ...
    def __next__(self): ...

class DictWriter:
    fieldnames = ...  # type: Any
    restval = ...  # type: Any
    extrasaction = ...  # type: Any
    writer = ...  # type: Any
    def __init__(
        self, f, fieldnames, restval=..., extrasaction=..., dialect=..., *args, **kwds
    ) -> None: ...
    def writeheader(self): ...
    def writerow(self, rowdict): ...
    def writerows(self, rowdicts): ...

class Sniffer:
    preferred = ...  # type: Any
    def __init__(self) -> None: ...
    def sniff(self, sample, delimiters=...): ...
    def has_header(self, sample): ...
