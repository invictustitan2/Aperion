# Stubs for http.server (Python 3.4)

import socketserver
from typing import Any, Optional, Tuple, Union

class HTTPServer(socketserver.TCPServer):
    server_name = ...  # type: str
    server_port = ...  # type: int
    def __init__(
        self, server_address: Tuple[str, int], RequestHandlerClass: type
    ) -> None: ...

class BaseHTTPRequestHandler:
    client_address = ...  # type: Tuple[str, int]
    server = ...  # type: socketserver.BaseServer
    close_connection = ...  # type: bool
    requestline = ...  # type: str
    command = ...  # type: str
    path = ...  # type: str
    request_version = ...  # type: str
    headers = ...  # type: email.message.Message
    rfile = ...  # type: BinaryIO
    wfile = ...  # type: BinaryIO
    server_version = ...  # type: str
    sys_version = ...  # type: str
    error_message_format = ...  # type: str
    error_content_type = ...  # type: str
    protocol_version = ...  # type: str
    MessageClass = ...  # type: type
    responses = ...  # type: Mapping[int, Tuple[str, str]]
    def __init__(
        self,
        request: bytes,
        client_address: Tuple[str, int],
        server: socketserver.BaseServer,
    ) -> None: ...
    def handle(self) -> None: ...
    def handle_one_request(self) -> None: ...
    def handle_expect_100(self) -> bool: ...
    def send_error(
        self, code: int, message: Optional[str] = ..., explain: Optional[str] = ...
    ) -> None: ...
    def send_response(self, code: int, message: Optional[str] = ...) -> None: ...
    def send_header(self, keyword: str, value: str) -> None: ...
    def send_response_only(self, code: int, message: Optional[str] = ...) -> None: ...
    def end_headers(self) -> None: ...
    def flush_headers(self) -> None: ...
    def log_request(
        self, code: Union[int, str] = ..., size: Union[int, str] = ...
    ) -> None: ...
    def log_error(self, format: str, *args: Any) -> None: ...
    def log_message(self, format: str, *args: Any) -> None: ...
    def version_string(self) -> str: ...
    def date_time_string(self, timestamp: Optional[int] = ...) -> str: ...
    def log_date_time_string(self) -> str: ...
    def address_string(self) -> str: ...

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    extensions_map = ...  # type: Dict[str, str]
    def __init__(
        self,
        request: bytes,
        client_address: Tuple[str, int],
        server: socketserver.BaseServer,
    ) -> None: ...
    def do_GET(self) -> None: ...
    def do_HEAD(self) -> None: ...

class CGIHTTPRequestHandler(SimpleHTTPRequestHandler):
    cgi_directories = ...  # type: List[str]
    def do_POST(self) -> None: ...
