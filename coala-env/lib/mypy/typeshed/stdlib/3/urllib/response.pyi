# private module, we only expose what's needed

from typing import BinaryIO, Mapping

class addinfourl(BinaryIO):
    def info(self) -> Mapping[str, str]: ...
    def geturl(self) -> str: ...
