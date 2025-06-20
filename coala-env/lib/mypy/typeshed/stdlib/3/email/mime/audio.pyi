# Stubs for email.mime.audio (Python 3.4)

from email.mime.nonmultipart import MIMENonMultipart
from typing import Callable, Optional, Tuple, Union

_ParamsType = Union[str, None, Tuple[str, Optional[str], str]]

class MIMEAudio(MIMENonMultipart):
    def __init__(
        self,
        _audiodata: bytes,
        _subtype: Optional[str] = ...,
        _encoder: Callable[[MIMEAudio], None] = ...,
        **_params: _ParamsType
    ) -> None: ...
