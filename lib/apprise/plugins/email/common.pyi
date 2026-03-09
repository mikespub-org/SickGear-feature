import dataclasses
from ...exception import ApprisePluginException as ApprisePluginException
from _typeshed import Incomplete

class AppriseEmailException(ApprisePluginException):
    """
    Thrown when there is an error with the Email Attachment
    """
    def __init__(self, message, error_code: int = 601) -> None: ...

class WebBaseLogin:
    """
    This class is just used in conjunction of the default emailers
    to best formulate a login to it using the data detected
    """
    EMAIL: str
    USERID: str

class SecureMailMode:
    INSECURE: str
    SSL: str
    STARTTLS: str

SECURE_MODES: Incomplete

@dataclasses.dataclass
class EmailMessage:
    """
    Our message structure
    """
    recipient: str
    to_addrs: list[str]
    body: str
