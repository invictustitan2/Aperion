# Stubs for requests.exceptions (Python 3)

from .packages.urllib3.exceptions import HTTPError as BaseHTTPError

class RequestException(IOError):
    response = ...  # type: Any
    request = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...

class HTTPError(RequestException): ...
class ConnectionError(RequestException): ...
class ProxyError(ConnectionError): ...
class SSLError(ConnectionError): ...
class Timeout(RequestException): ...
class ConnectTimeout(ConnectionError, Timeout): ...
class ReadTimeout(Timeout): ...
class URLRequired(RequestException): ...
class TooManyRedirects(RequestException): ...
class MissingSchema(RequestException, ValueError): ...
class InvalidSchema(RequestException, ValueError): ...
class InvalidURL(RequestException, ValueError): ...
class ChunkedEncodingError(RequestException): ...
class ContentDecodingError(RequestException, BaseHTTPError): ...
class StreamConsumedError(RequestException, TypeError): ...
class RetryError(RequestException): ...
