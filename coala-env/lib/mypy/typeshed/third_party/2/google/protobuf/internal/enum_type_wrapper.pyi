from typing import Any, List, Tuple

class EnumTypeWrapper(object):
    def __init__(self, enum_type: Any) -> None: ...
    def Name(self, number: int) -> str: ...
    def Value(self, name: str) -> int: ...
    def keys(self) -> List[str]: ...
    def values(self) -> List[int]: ...
    @classmethod
    def items(cls) -> List[Tuple[str, int]]: ...
