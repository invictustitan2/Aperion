from typing import AnyStr

from . import visitors
from .base import DialectKWArgs, SchemaEventTarget
from .elements import ColumnClause
from .selectable import TableClause

class SchemaItem(SchemaEventTarget, visitors.Visitable):
    def _execute_on_connection(self, connection, multiparams, params): ...
    @property
    def info(self): ...
    @property
    def quote(self): ...
    def get_children(self, **kwargs): ...
    def _init_items(self, *args): ...
    def _schema_item_copy(self, schema_item): ...
    def __repr__(self): ...

class Table(DialectKWArgs, SchemaItem, TableClause):
    def __init__(self, name, metadata, *args, **kwargs): ...
    @property
    def key(self): ...
    @property
    def primary_key(self): ...
    def __repr__(self): ...
    def __str__(self): ...
    def append_column(self, column): ...
    def append_constraint(self, constraint): ...
    def append_ddl_listener(self, event, listener): ...
    def get_children(self, column_collections=True, schema_visitor=False, **kwargs): ...
    def exists(self, bind=None): ...
    def create(self, bind=None, checkfirst=False): ...
    def drop(self, bind=None, checkfirst=False): ...
    def tometadata(self, metadata, schema=None): ...
    c = ...  # type: ColumnCollection
    constraints = ...  # type: Set[Constraint]

class Column(SchemaItem, ColumnClause):
    primary_key = ...  # type: Any
    def __init__(self, *args, **kwargs): ...
    def references(self, column): ...
    def append_foreign_key(self, fk): ...
    def __repr__(self): ...
    def _set_parent(self, table): ...
    def _setup_on_memoized_fks(self, fn): ...
    def _on_table_attach(self, fn): ...
    def copy(self, **kw): ...
    def _make_proxy(
        self, selectable, name=None, key=None, name_is_truncatable=False, **kw
    ): ...
    def get_children(self, schema_visitor=False, **kwargs): ...

class ForeignKey(DialectKWArgs, SchemaItem):
    def __init__(
        self,
        column,
        _constraint=None,
        use_alter=False,
        name=None,
        onupdate=None,
        ondelete=None,
        deferrable=None,
        initially=None,
        link_to_name=False,
        match=None,
        info=None,
        **dialect_kw
    ) -> None: ...
    def __repr__(self): ...
    def copy(self, schema=None): ...
    def _get_colspec(self, schema=None, table_name=None): ...
    @property
    def _referred_schema(self): ...
    def _table_key(self): ...
    def references(self, table): ...
    def get_referent(self, table): ...
    @property
    def _column_tokens(self): ...
    def _resolve_col_tokens(self): ...
    def _link_to_col_by_colstring(self, parenttable, table, colname): ...
    def _set_target_column(self, column): ...
    @property
    def column(self): ...
    def _set_parent(self, column): ...
    def _set_remote_table(self, table): ...
    def _remove_from_metadata(self, metadata): ...
    def _set_table(self, column, table): ...

class _NotAColumnExpr(object): ...
class DefaultGenerator(_NotAColumnExpr, SchemaItem): ...
class ColumnDefault(DefaultGenerator): ...
class Sequence(DefaultGenerator): ...
class FetchedValue(_NotAColumnExpr, SchemaEventTarget): ...
class DefaultClause(FetchedValue): ...
class PassiveDefault(DefaultClause): ...

class Constraint(DialectKWArgs, SchemaItem):
    def __init__(self, name=None, deferrable=None, initially=None): ...
    def __contains__(self, x): ...
    def contains_column(self, col): ...
    def keys(self): ...
    def __add__(self, other): ...
    def __iter__(self): ...
    def __len__(self): ...
    def copy(self, **kw): ...

class ColumnCollectionMixin(object):
    columns = ...  # type: Any
    def __init__(self, *columns, **kw): ...
    @classmethod
    def _extract_col_expression_collection(cls, expressions): ...
    def _check_attach(self, evt=False): ...
    def _set_parent(self, table): ...

class ColumnCollectionConstraint(ColumnCollectionMixin, Constraint):
    def __init__(self, *columns, **kw): ...
    def _set_parent(self, table): ...
    def __contains__(self, x): ...
    def copy(self, **kw): ...
    def contains_column(self, col): ...
    def __iter__(self): ...
    def __len__(self): ...

class CheckConstraint(ColumnCollectionConstraint): ...
class ForeignKeyConstraint(ColumnCollectionConstraint): ...
class PrimaryKeyConstraint(ColumnCollectionConstraint): ...
class UniqueConstraint(ColumnCollectionConstraint): ...
class Index(DialectKWArgs, ColumnCollectionMixin, SchemaItem): ...
class MetaData(SchemaItem): ...
class ThreadLocalMetaData(MetaData): ...

def _get_table_key(name: AnyStr, schema: AnyStr): ...
