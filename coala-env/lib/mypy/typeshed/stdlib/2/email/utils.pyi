# Stubs for email.utils (Python 2)
#
# Derived from stub automatically generated by stubgen.

from email._parseaddr import mktime_tz as mktime_tz

def formataddr(pair): ...
def getaddresses(fieldvalues): ...
def formatdate(timeval=None, localtime=False, usegmt=False): ...
def make_msgid(idstring=None): ...
def parsedate(data): ...
def parsedate_tz(data): ...
def parseaddr(addr): ...
def unquote(str): ...
def decode_rfc2231(s): ...
def encode_rfc2231(s, charset=None, language=None): ...
def decode_params(params): ...
def collapse_rfc2231_value(value, errors=..., fallback_charset=...): ...
