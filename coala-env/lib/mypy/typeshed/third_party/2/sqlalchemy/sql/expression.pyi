# Stubs for sqlalchemy.sql.expression (Python 2)


from . import functions

func = functions.func # type: functions._FunctionGenerator
modifier = functions.modifier # type: functions._FunctionGenerator

from .base import Executable, Generative
from .elements import (BinaryExpression, BindParameter, Case, Cast, Extract, False_, Grouping, Label, Null, Over, TextClause,
                       True_, Tuple, TypeClause, UnaryExpression)
from .selectable import (Exists, FromGrouping, ScalarSelect, SelectBase)

and_ = ... # type: Any
or_ = ... # type: Any
bindparam = ... # type: Any
select = ... # type: Any
text = ... # type: Any
table = ... # type: Any
column = ... # type: Any
over = ... # type: Any
label = ... # type: Any
case = ... # type: Any
cast = ... # type: Any
extract = ... # type: Any
tuple_ = ... # type: Any
except_ = ... # type: Any
except_all = ... # type: Any
intersect = ... # type: Any
intersect_all = ... # type: Any
union = ... # type: Any
union_all = ... # type: Any
exists = ... # type: Any
nullsfirst = ... # type: Any
nullslast = ... # type: Any
asc = ... # type: Any
desc = ... # type: Any
distinct = ... # type: Any
true = ... # type: Any
false = ... # type: Any
null = ... # type: Any
join = ... # type: Any
outerjoin = ... # type: Any
insert = ... # type: Any
update = ... # type: Any
delete = ... # type: Any
funcfilter = ... # type: Any

# old names for compatibility
_Executable = Executable
_BindParamClause = BindParameter
_Label = Label
_SelectBase = SelectBase
_BinaryExpression = BinaryExpression
_Cast = Cast
_Null = Null
_False = False_
_True = True_
_TextClause = TextClause
_UnaryExpression = UnaryExpression
_Case = Case
_Tuple = Tuple
_Over = Over
_Generative = Generative
_TypeClause = TypeClause
_Extract = Extract
_Exists = Exists
_Grouping = Grouping
_FromGrouping = FromGrouping
_ScalarSelect = ScalarSelect
