# Stubs for logging.config (Python 3.4)

import sys
from typing import IO, Any, Callable, Dict, Optional, Union

if sys.version_info >= (3,):
    # from configparser import RawConfigParser
    # TODO add RawConfigParser to configparser stubs
    RawConfigParser = Any
else:
    from ConfigParser import RawConfigParser

def dictConfig(config: Dict[str, Any]) -> None: ...

if sys.version_info >= (3, 4):
    def fileConfig(
        fname: Union[str, IO[str], RawConfigParser],
        defaults: Optional[Dict[str, str]] = ...,
        disable_existing_loggers: bool = ...,
    ) -> None: ...
    def listen(
        port: int = ..., verify: Optional[Callable[[bytes], Optional[bytes]]] = ...
    ) -> None: ...

else:
    def fileConfig(
        fname: Union[str, IO[str]],
        defaults: Optional[Dict[str, str]] = ...,
        disable_existing_loggers: bool = ...,
    ) -> None: ...
    def listen(port: int = ...) -> None: ...

def stopListening() -> None: ...
