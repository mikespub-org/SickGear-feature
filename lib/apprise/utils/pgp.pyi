from ..apprise_attachment import AppriseAttachment as AppriseAttachment
from ..asset import AppriseAsset as AppriseAsset
from ..exception import ApprisePluginException as ApprisePluginException
from ..logger import logger as logger
from _typeshed import Incomplete

PGP_SUPPORT: bool

class ApprisePGPException(ApprisePluginException):
    """Thrown when there is an error with the Pretty Good Privacy
    Controller."""
    def __init__(self, message, error_code: int = 602) -> None: ...

class ApprisePGPController:
    """Pretty Good Privacy Controller Tool for the Apprise Library."""
    max_pgp_public_key_size: int
    __key_lookup: Incomplete
    path: Incomplete
    email: Incomplete
    asset: Incomplete
    _pub_keyfile: Incomplete
    def __init__(self, path, pub_keyfile=None, email=None, asset=None, **kwargs) -> None:
        """Path should be the directory keys can be written and read from such
        as <notifyobject>.store.path.

        Optionally additionally specify a keyfile to explicitly open
        """
    def keygen(self, email=None, name=None, force: bool = False):
        """Generates a set of keys based on email configured."""
    def public_keyfile(self, *emails):
        """Returns the first match of a useable public key based emails
        provided."""
    def public_key(self, *emails, autogen=None):
        """Opens a spcified pgp public file and returns the key from it which
        is used to encrypt the message."""
    def encrypt(self, message, *emails):
        """If provided a path to a pgp-key, content is encrypted."""
    def prune(self) -> None:
        """Prunes old entries from the public_key index."""
    @property
    def pub_keyfile(self):
        """Returns the Public Keyfile Path if set otherwise it returns None
        This property returns False if a keyfile was provided, but was
        invalid."""
