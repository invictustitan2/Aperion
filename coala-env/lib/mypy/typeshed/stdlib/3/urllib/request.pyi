# Stubs for urllib.request (Python 3.4)

import ssl
import sys
from email.message import Message
from http.client import HTTPMessage, HTTPResponse
from http.cookiejar import CookieJar
from typing import (
    IO,
    Any,
    Callable,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
    overload,
)
from urllib.response import addinfourl

_T = TypeVar("_T")
_UrlopenRet = Union[HTTPResponse, addinfourl]

def urlopen(
    url: Union[str, "Request"],
    data: Optional[bytes] = ...,
    timeout: float = ...,
    *,
    cafile: Optional[str] = ...,
    capath: Optional[str] = ...,
    cadefault: bool = ...,
    context: Optional[ssl.SSLContext] = ...
) -> _UrlopenRet: ...
def install_opener(opener: OpenerDirector) -> None: ...
def build_opener(
    *handlers: Union[BaseHandler, Callable[[], BaseHandler]]
) -> OpenerDirector: ...
def url2pathname(path: str) -> str: ...
def pathname2url(path: str) -> str: ...
def getproxies() -> Dict[str, str]: ...
def parse_http_list(s: str) -> List[str]: ...

class Request:
    if sys.version_info >= (3, 4):
        @property
        def full_url(self) -> str: ...
        @full_url.setter
        def full_url(self, value: str) -> None: ...
        @full_url.deleter
        def full_url(self) -> None: ...
    else:
        full_url = ...  # type: str
    type = ...  # type: str
    host = ...  # type: str
    origin_req_host = ...  # type: str
    selector = ...  # type: str
    data = ...  # type: Optional[bytes]
    unverifiable = ...  # type: bool
    method = ...  # type: Optional[str]
    def __init__(
        self,
        url: str,
        data: Optional[bytes] = ...,
        headers: Dict[str, str] = ...,
        origin_req_host: Optional[str] = ...,
        unverifiable: bool = ...,
        method: Optional[str] = ...,
    ) -> None: ...
    def get_method(self) -> str: ...
    def add_header(self, key: str, val: str) -> None: ...
    def add_unredirected_header(self, key: str, val: str) -> None: ...
    def has_header(self, header_name: str) -> bool: ...
    if sys.version_info >= (3, 4):
        def remove_header(self, header_name: str) -> None: ...

    def get_full_url(self) -> str: ...
    def set_proxy(self, host: str, type: str) -> None: ...
    @overload
    def get_header(self, header_name: str) -> Optional[str]: ...
    @overload
    def get_header(self, header_name: str, default: _T) -> Union[str, _T]: ...
    def header_items(self) -> List[Tuple[str, str]]: ...

class OpenerDirector:
    def add_handler(self, handler: BaseHandler) -> None: ...
    def open(
        self,
        url: Union[str, Request],
        data: Optional[bytes] = None,
        timeout: float = ...,
    ) -> _UrlopenRet: ...
    def error(self, proto: str, *args: Any) -> _UrlopenRet: ...

class BaseHandler:
    parent = ...  # type: OpenerDirector
    def add_parent(self, parent: OpenerDirector) -> None: ...
    def close(self) -> None: ...
    def http_error_nnn(
        self, req: Request, fp: IO[str], code: int, msg: int, hdrs: Mapping[str, str]
    ) -> _UrlopenRet: ...

class HTTPDefaultErrorHandler(BaseHandler): ...

class HTTPRedirectHandler(BaseHandler):
    def redirect_request(
        self,
        req: Request,
        fp: IO[str],
        code: int,
        msg: int,
        hdrs: Mapping[str, str],
        newurl: str,
    ) -> Optional[Request]: ...
    def http_error_301(
        self, req: Request, fp: IO[str], code: int, msg: int, hdrs: Mapping[str, str]
    ) -> Optional[_UrlopenRet]: ...
    def http_error_302(
        self, req: Request, fp: IO[str], code: int, msg: int, hdrs: Mapping[str, str]
    ) -> Optional[_UrlopenRet]: ...
    def http_error_303(
        self, req: Request, fp: IO[str], code: int, msg: int, hdrs: Mapping[str, str]
    ) -> Optional[_UrlopenRet]: ...
    def http_error_307(
        self, req: Request, fp: IO[str], code: int, msg: int, hdrs: Mapping[str, str]
    ) -> Optional[_UrlopenRet]: ...

class HTTPCookieProcessor(BaseHandler):
    cookiejar = ...  # type: CookieJar
    def __init__(self, cookiejar: Optional[CookieJar] = ...) -> None: ...

class ProxyHandler(BaseHandler):
    def __init__(self, proxies: Optional[Dict[str, str]] = ...) -> None: ...
    # TODO add a method for every (common) proxy protocol

class HTTPPasswordMgr:
    def add_password(
        self, realm: str, uri: Union[str, Sequence[str]], user: str, passwd: str
    ) -> None: ...
    def find_user_password(
        self, realm: str, authuri: str
    ) -> Tuple[Optional[str], Optional[str]]: ...

class HTTPPasswordMgrWithDefaultRealm:
    def add_password(
        self, realm: str, uri: Union[str, Sequence[str]], user: str, passwd: str
    ) -> None: ...
    def find_user_password(
        self, realm: str, authuri: str
    ) -> Tuple[Optional[str], Optional[str]]: ...

if sys.version_info >= (3, 5):
    class HTTPPasswordMgrWithPriorAuth(HTTPPasswordMgrWithDefaultRealm):
        def add_password(
            self,
            realm: str,
            uri: Union[str, Sequence[str]],
            user: str,
            passwd: str,
            is_authenticated: bool = ...,
        ) -> None: ...
        def update_authenticated(
            self, uri: Union[str, Sequence[str]], is_authenticated: bool = ...
        ) -> None: ...
        def is_authenticated(self, authuri: str) -> bool: ...

class AbstractBasicAuthHandler:
    def __init__(self, password_mgr: Optional[HTTPPasswordMgr] = ...) -> None: ...
    def http_error_auth_reqed(
        self, authreq: str, host: str, req: Request, headers: Mapping[str, str]
    ) -> None: ...

class HTTPBasicAuthHandler(AbstractBasicAuthHandler, BaseHandler):
    def http_error_401(
        self, req: Request, fp: IO[str], code: int, msg: int, hdrs: Mapping[str, str]
    ) -> Optional[_UrlopenRet]: ...

class ProxyBasicAuthHandler(AbstractBasicAuthHandler, BaseHandler):
    def http_error_407(
        self, req: Request, fp: IO[str], code: int, msg: int, hdrs: Mapping[str, str]
    ) -> Optional[_UrlopenRet]: ...

class AbstractDigestAuthHandler:
    def __init__(self, password_mgr: Optional[HTTPPasswordMgr] = ...) -> None: ...
    def http_error_auth_reqed(
        self, auth_header: str, host: str, req: Request, headers: Mapping[str, str]
    ) -> None: ...

class HTTPDigestAuthHandler(BaseHandler, AbstractDigestAuthHandler):
    def http_error_401(
        self, req: Request, fp: IO[str], code: int, msg: int, hdrs: Mapping[str, str]
    ) -> Optional[_UrlopenRet]: ...

class ProxyDigestAuthHandler(BaseHandler, AbstractDigestAuthHandler):
    def http_error_407(
        self, req: Request, fp: IO[str], code: int, msg: int, hdrs: Mapping[str, str]
    ) -> Optional[_UrlopenRet]: ...

class HTTPHandler(BaseHandler):
    def http_open(self, req: Request) -> _UrlopenRet: ...

class HTTPSHandler(BaseHandler):
    def __init__(
        self,
        debuglevel: int = 0,
        context: Optional[ssl.SSLContext] = ...,
        check_hostname: bool = ...,
    ) -> None: ...
    def https_open(self, req: Request) -> _UrlopenRet: ...

class FileHandler(BaseHandler):
    def file_open(self, req: Request) -> _UrlopenRet: ...

class DataHandler(BaseHandler):
    def data_open(self, req: Request) -> _UrlopenRet: ...

class FTPHandler(BaseHandler):
    def ftp_open(self, req: Request) -> _UrlopenRet: ...

class CacheFTPHandler(FTPHandler):
    def setTimeout(self, t: float) -> None: ...
    def setMaxConns(self, m: int) -> None: ...

class UnknownHandler(BaseHandler):
    def unknown_open(self, req: Request) -> _UrlopenRet: ...

class HTTPErrorProcessor(BaseHandler):
    def http_response(self) -> _UrlopenRet: ...
    def https_response(self) -> _UrlopenRet: ...

def urlretrieve(
    url: str,
    filename: Optional[str] = ...,
    reporthook: Optional[Callable[[int, int, int], None]] = ...,
    data: Optional[bytes] = ...,
) -> Tuple[str, HTTPMessage]: ...
def urlcleanup() -> None: ...

class URLopener:
    version = ...  # type: str
    def __init__(
        self, proxies: Optional[Dict[str, str]] = ..., **x509: str
    ) -> None: ...
    def open(self, fullurl: str, data: Optional[bytes] = ...) -> _UrlopenRet: ...
    def open_unknown(
        self, fullurl: str, data: Optional[bytes] = ...
    ) -> _UrlopenRet: ...
    def retrieve(
        self,
        url: str,
        filename: Optional[str] = ...,
        reporthook: Optional[Callable[[int, int, int], None]] = ...,
        data: Optional[bytes] = ...,
    ) -> Tuple[str, Optional[Message]]: ...

class FancyURLopener(URLopener):
    def prompt_user_passwd(self, host: str, realm: str) -> Tuple[str, str]: ...
