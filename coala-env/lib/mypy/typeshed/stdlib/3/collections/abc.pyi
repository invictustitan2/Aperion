# Stubs for collections.abc (introduced from Python 3.3)
#
# https://docs.python.org/3.3/whatsnew/3.3.html#collections
import sys

if sys.version_info >= (3, 3):
    from . import Container as Container
    from . import MutableMapping as MutableMapping
    from . import MutableSequence as MutableSequence
    from . import MutableSet as MutableSet
    from . import Sequence as Sequence
    from . import Set as Set
