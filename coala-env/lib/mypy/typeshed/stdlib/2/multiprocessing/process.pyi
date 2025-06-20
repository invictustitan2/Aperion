# Stubs for multiprocessing.process (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

def current_process(): ...
def active_children(): ...

class Process:
    def __init__(self, group=None, target=None, name=None, args=..., kwargs=...): ...
    def run(self): ...
    def start(self): ...
    def terminate(self): ...
    def join(self, timeout=None): ...
    def is_alive(self): ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name): ...
    @property
    def daemon(self): ...
    @daemon.setter
    def daemon(self, daemonic): ...
    @property
    def authkey(self): ...
    @authkey.setter
    def authkey(self, authkey): ...
    @property
    def exitcode(self): ...
    @property
    def ident(self): ...
    pid = ...  # type: Any

class AuthenticationString(bytes):
    def __reduce__(self): ...

class _MainProcess(Process):
    def __init__(self): ...
