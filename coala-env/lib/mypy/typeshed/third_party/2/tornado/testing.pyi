# Stubs for tornado.testing (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import logging
import unittest

AsyncHTTPClient = ...  # type: Any
gen = ...  # type: Any
HTTPServer = ...  # type: Any
IOLoop = ...  # type: Any
netutil = ...  # type: Any
SimpleAsyncHTTPClient = ...  # type: Any

def get_unused_port(): ...
def bind_unused_port(): ...

class AsyncTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs): ...
    io_loop = ...  # type: Any
    def setUp(self): ...
    def tearDown(self): ...
    def get_new_ioloop(self): ...
    def run(self, result=None): ...
    def stop(self, _arg=None, **kwargs): ...
    def wait(self, condition=None, timeout=5): ...

class AsyncHTTPTestCase(AsyncTestCase):
    http_client = ...  # type: Any
    http_server = ...  # type: Any
    def setUp(self): ...
    def get_http_client(self): ...
    def get_http_server(self): ...
    def get_app(self): ...
    def fetch(self, path, **kwargs): ...
    def get_httpserver_options(self): ...
    def get_http_port(self): ...
    def get_protocol(self): ...
    def get_url(self, path): ...
    def tearDown(self): ...

class AsyncHTTPSTestCase(AsyncHTTPTestCase):
    def get_http_client(self): ...
    def get_httpserver_options(self): ...
    def get_ssl_options(self): ...
    def get_protocol(self): ...

def gen_test(f): ...

class LogTrapTestCase(unittest.TestCase):
    def run(self, result=None): ...

class ExpectLog(logging.Filter):
    logger = ...  # type: Any
    regex = ...  # type: Any
    required = ...  # type: Any
    matched = ...  # type: Any
    def __init__(self, logger, regex, required=True): ...
    def filter(self, record): ...
    def __enter__(self): ...
    def __exit__(self, typ, value, tb): ...

def main(**kwargs): ...
