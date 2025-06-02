# Stubs for email.contentmanager (Python 3.4)

import email.message
import sys
from email.message import Message
from typing import Any, Callable

if sys.version_info >= (3, 4):

    EmailMessage = email.message.EmailMessage
    MIMEPart = email.message.MIMEPart

    class ContentManager:
        def __init__(self) -> None: ...
        def get_content(self, msg: Message, *args: Any, **kw: Any) -> Any: ...
        def set_content(self, msg: Message, obj: Any, *args: Any, **kw: Any) -> Any: ...
        def add_get_handler(self, key: str, handler: Callable[..., Any]) -> None: ...
        def add_set_handler(
            self, typekey: type, handler: Callable[..., Any]
        ) -> None: ...

    raw_data_manager = ...  # type: ContentManager
