from typing import Tuple

class ParserBase(object):
    def __init__(self) -> None: ...
    def error(self, message: str) -> None: ...
    def reset(self) -> None: ...
    def getpos(self) -> Tuple[int, int]: ...
    def unkown_decl(self, data: str) -> None: ...
