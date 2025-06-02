# Stubs for rlcompleter

import sys
from typing import Optional, Union

if sys.version_info >= (3,):
    _Text = str
else:
    _Text = Union[str, unicode]

class Completer:
    def complete(self, text: _Text, state: int) -> Optional[str]: ...
