from . import shim
from _typeshed import Incomplete

__all__ = ['GNTPRegister', 'GNTPNotice', 'GNTPSubscribe', 'GNTPOK', 'GNTPError', 'parse_gntp']

class _GNTPBuffer(shim.StringIO):
    """GNTP Buffer class"""
    def writeln(self, value=None) -> None: ...
    def writeheader(self, key, value) -> None: ...

class _GNTPBase:
    """Base initilization

\t:param string messagetype: GNTP Message type
\t:param string version: GNTP Protocol version
\t:param string encription: Encryption protocol
\t"""
    info: Incomplete
    hash_algo: Incomplete
    headers: Incomplete
    resources: Incomplete
    def __init__(self, messagetype=None, version: str = '1.0', encryption=None) -> None: ...
    def __str__(self) -> str: ...
    def _parse_info(self, data):
        """Parse the first line of a GNTP message to get security and other info values

\t\t:param string data: GNTP Message
\t\t:return dict: Parsed GNTP Info line
\t\t"""
    password: Incomplete
    encryptAlgo: Incomplete
    def set_password(self, password, encryptAlgo: str = 'MD5') -> None:
        """Set a password for a GNTP Message

\t\t:param string password: Null to clear password
\t\t:param string encryptAlgo: Supports MD5, SHA1, SHA256, SHA512
\t\t"""
    def _decode_hex(self, value):
        """Helper function to decode hex string to `proper` hex string

\t\t:param string value: Human readable hex string
\t\t:return string: Hex string
\t\t"""
    def _decode_binary(self, rawIdentifier, identifier): ...
    key: Incomplete
    def _validate_password(self, password):
        """Validate GNTP Message against stored password"""
    def validate(self) -> None:
        """Verify required headers"""
    def _format_info(self):
        """Generate info line for GNTP Message

\t\t:return string:
\t\t"""
    def _parse_dict(self, data):
        """Helper function to parse blocks of GNTP headers into a dictionary

\t\t:param string data:
\t\t:return dict: Dictionary of parsed GNTP Headers
\t\t"""
    def add_header(self, key, value) -> None: ...
    def add_resource(self, data):
        """Add binary resource

\t\t:param string data: Binary Data
\t\t"""
    raw: Incomplete
    def decode(self, data, password=None) -> None:
        """Decode GNTP Message

\t\t:param string data:
\t\t"""
    def encode(self):
        """Encode a generic GNTP Message

\t\t:return string: GNTP Message ready to be sent. Returned as a byte string
\t\t"""

class GNTPRegister(_GNTPBase):
    """Represents a GNTP Registration Command

\t:param string data: (Optional) See decode()
\t:param string password: (Optional) Password to use while encoding/decoding messages
\t"""
    _requiredHeaders: Incomplete
    _requiredNotificationHeaders: Incomplete
    notifications: Incomplete
    def __init__(self, data=None, password=None) -> None: ...
    def validate(self) -> None:
        """Validate required headers and validate notification headers"""
    raw: Incomplete
    info: Incomplete
    headers: Incomplete
    def decode(self, data, password) -> None:
        """Decode existing GNTP Registration message

\t\t:param string data: Message to decode
\t\t"""
    def add_notification(self, name, enabled: bool = True) -> None:
        """Add new Notification to Registration message

\t\t:param string name: Notification Name
\t\t:param boolean enabled: Enable this notification by default
\t\t"""
    def encode(self):
        """Encode a GNTP Registration Message

\t\t:return string: Encoded GNTP Registration message. Returned as a byte string
\t\t"""

class GNTPNotice(_GNTPBase):
    """Represents a GNTP Notification Command

\t:param string data: (Optional) See decode()
\t:param string app: (Optional) Set Application-Name
\t:param string name: (Optional) Set Notification-Name
\t:param string title: (Optional) Set Notification Title
\t:param string password: (Optional) Password to use while encoding/decoding messages
\t"""
    _requiredHeaders: Incomplete
    def __init__(self, data=None, app=None, name=None, title=None, password=None) -> None: ...
    raw: Incomplete
    info: Incomplete
    headers: Incomplete
    def decode(self, data, password) -> None:
        """Decode existing GNTP Notification message

\t\t:param string data: Message to decode.
\t\t"""

class GNTPSubscribe(_GNTPBase):
    """Represents a GNTP Subscribe Command

\t:param string data: (Optional) See decode()
\t:param string password: (Optional) Password to use while encoding/decoding messages
\t"""
    _requiredHeaders: Incomplete
    def __init__(self, data=None, password=None) -> None: ...

class GNTPOK(_GNTPBase):
    """Represents a GNTP OK Response

\t:param string data: (Optional) See _GNTPResponse.decode()
\t:param string action: (Optional) Set type of action the OK Response is for
\t"""
    _requiredHeaders: Incomplete
    def __init__(self, data=None, action=None) -> None: ...

class GNTPError(_GNTPBase):
    """Represents a GNTP Error response

\t:param string data: (Optional) See _GNTPResponse.decode()
\t:param string errorcode: (Optional) Error code
\t:param string errordesc: (Optional) Error Description
\t"""
    _requiredHeaders: Incomplete
    def __init__(self, data=None, errorcode=None, errordesc=None) -> None: ...
    def error(self): ...

def parse_gntp(data, password=None):
    """Attempt to parse a message as a GNTP message

\t:param string data: Message to be parsed
\t:param string password: Optional password to be used to verify the message
\t"""
