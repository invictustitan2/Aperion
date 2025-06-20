# Stubs for socketserver

import sys
import types
from typing import Optional, Tuple

class BaseServer:
    address_family = ...  # type: int
    RequestHandlerClass = ...  # type: type
    server_address = ...  # type: Tuple[str, int]
    socket = ...  # type: SocketType
    allow_reuse_address = ...  # type: bool
    request_queue_size = ...  # type: int
    socket_type = ...  # type: int
    timeout = ...  # type: Optional[float]
    def __init__(
        self, server_address: Tuple[str, int], RequestHandlerClass: type
    ) -> None: ...
    def fileno(self) -> int: ...
    def handle_request(self) -> None: ...
    def serve_forever(self, poll_interval: float = ...) -> None: ...
    def shutdown(self) -> None: ...
    def server_close(self) -> None: ...
    def finish_request(self) -> None: ...
    def get_request(self) -> None: ...
    def handle_error(self, request: bytes, client_address: Tuple[str, int]) -> None: ...
    def handle_timeout(self) -> None: ...
    def process_request(
        self, request: bytes, client_address: Tuple[str, int]
    ) -> None: ...
    def server_activate(self) -> None: ...
    def server_bind(self) -> None: ...
    def verify_request(
        self, request: bytes, client_address: Tuple[str, int]
    ) -> bool: ...
    if sys.version_info >= (3, 6):
        def __enter__(self) -> "BaseServer": ...
        def __exit__(
            self,
            exc_type: Optional[type],
            exc_val: Optional[Exception],
            exc_tb: Optional[types.TracebackType],
        ) -> bool: ...
    if sys.version_info >= (3, 3):
        def service_actions(self) -> None: ...

class TCPServer(BaseServer):
    def __init__(
        self,
        server_address: Tuple[str, int],
        RequestHandlerClass: type,
        bind_and_activate: bool = ...,
    ) -> None: ...

class UDPServer(BaseServer):
    def __init__(
        self,
        server_address: Tuple[str, int],
        RequestHandlerClass: type,
        bind_and_activate: bool = ...,
    ) -> None: ...

class UnixStreamServer(BaseServer):
    def __init__(
        self,
        server_address: Tuple[str, int],
        RequestHandlerClass: type,
        bind_and_activate: bool = ...,
    ) -> None: ...

class UnixDatagramServer(BaseServer):
    def __init__(
        self,
        server_address: Tuple[str, int],
        RequestHandlerClass: type,
        bind_and_activate: bool = ...,
    ) -> None: ...

class ForkingMixIn: ...
class ThreadingMixIn: ...
class ForkingTCPServer(ForkingMixIn, TCPServer): ...
class ForkingUDPServer(ForkingMixIn, UDPServer): ...
class ThreadingTCPServer(ThreadingMixIn, TCPServer): ...
class ThreadingUDPServer(ThreadingMixIn, UDPServer): ...

class BaseRequestHandler:
    # Those are technically of types, respectively:
    # * Union[SocketType, Tuple[bytes, SocketType]]
    # * Union[Tuple[str, int], str]
    # But there are some concerns that having unions here would cause
    # too much inconvenience to people using it (see
    # https://github.com/python/typeshed/pull/384#issuecomment-234649696)
    request = ...  # type: Any
    client_address = ...  # type: Any

    server = ...  # type: BaseServer
    def setup(self) -> None: ...
    def handle(self) -> None: ...
    def finish(self) -> None: ...

class StreamRequestHandler(BaseRequestHandler):
    rfile = ...  # type: BinaryIO
    wfile = ...  # type: BinaryIO

class DatagramRequestHandler(BaseRequestHandler):
    rfile = ...  # type: BinaryIO
    wfile = ...  # type: BinaryIO
