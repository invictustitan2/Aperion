# Stubs for getpass

from typing import TextIO

def getpass(prompt: str = ..., stream: TextIO = None) -> str: ...
def getuser() -> str: ...

class GetPassWarning(UserWarning):
    pass
