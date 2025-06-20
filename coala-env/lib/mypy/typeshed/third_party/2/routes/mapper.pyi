# Stubs for routes.mapper (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

COLLECTION_ACTIONS = ...  # type: Any
MEMBER_ACTIONS = ...  # type: Any

def strip_slashes(name): ...

class SubMapperParent:
    def submapper(self, **kargs): ...
    def collection(
        self,
        collection_name,
        resource_name,
        path_prefix=...,
        member_prefix=...,
        controller=...,
        collection_actions=...,
        member_actions=...,
        member_options=...,
        **kwargs
    ): ...

class SubMapper(SubMapperParent):
    kwargs = ...  # type: Any
    obj = ...  # type: Any
    collection_name = ...  # type: Any
    member = ...  # type: Any
    resource_name = ...  # type: Any
    formatted = ...  # type: Any
    def __init__(
        self,
        obj,
        resource_name=...,
        collection_name=...,
        actions=...,
        formatted=...,
        **kwargs
    ) -> None: ...
    def connect(self, *args, **kwargs): ...
    def link(
        self, rel=..., name=..., action=..., method=..., formatted=..., **kwargs
    ): ...
    def new(self, **kwargs): ...
    def edit(self, **kwargs): ...
    def action(self, name=..., action=..., method=..., formatted=..., **kwargs): ...
    def index(self, name=..., **kwargs): ...
    def show(self, name=..., **kwargs): ...
    def create(self, **kwargs): ...
    def update(self, **kwargs): ...
    def delete(self, **kwargs): ...
    def add_actions(self, actions): ...
    def __enter__(self): ...
    def __exit__(self, type, value, tb): ...

class Mapper(SubMapperParent):
    matchlist = ...  # type: Any
    maxkeys = ...  # type: Any
    minkeys = ...  # type: Any
    urlcache = ...  # type: Any
    prefix = ...  # type: Any
    req_data = ...  # type: Any
    directory = ...  # type: Any
    always_scan = ...  # type: Any
    controller_scan = ...  # type: Any
    debug = ...  # type: Any
    append_slash = ...  # type: Any
    sub_domains = ...  # type: Any
    sub_domains_ignore = ...  # type: Any
    domain_match = ...  # type: Any
    explicit = ...  # type: Any
    encoding = ...  # type: Any
    decode_errors = ...  # type: Any
    hardcode_names = ...  # type: Any
    minimization = ...  # type: Any
    create_regs_lock = ...  # type: Any
    def __init__(
        self,
        controller_scan=...,
        directory=...,
        always_scan=...,
        register=...,
        explicit=...,
    ) -> None: ...
    environ = ...  # type: Any
    def extend(self, routes, path_prefix=...): ...
    def make_route(self, *args, **kargs): ...
    def connect(self, *args, **kargs): ...
    def create_regs(self, *args, **kwargs): ...
    def match(self, url=..., environ=...): ...
    def routematch(self, url=..., environ=...): ...
    obj = ...  # type: Any
    def generate(self, *args, **kargs): ...
    def resource(self, member_name, collection_name, **kwargs): ...
    def redirect(self, match_path, destination_path, *args, **kwargs): ...
