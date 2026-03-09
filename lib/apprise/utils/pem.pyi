from ..apprise_attachment import AppriseAttachment as AppriseAttachment
from ..asset import AppriseAsset as AppriseAsset
from ..exception import ApprisePluginException as ApprisePluginException
from ..logger import logger as logger
from ..utils.base64 import base64_urldecode as base64_urldecode, base64_urlencode as base64_urlencode
from _typeshed import Incomplete
from cryptography.hazmat.primitives.asymmetric import ec

PEM_SUPPORT: bool

class ApprisePEMException(ApprisePluginException):
    """Thrown when there is an error with the PEM Controller."""
    def __init__(self, message, error_code: int = 612) -> None: ...

class ApprisePEMController:
    """PEM Controller Tool for the Apprise Library."""
    max_pem_public_key_size: int
    max_pem_private_key_size: int
    max_webpush_record_size: int
    path: Incomplete
    __private_key: Incomplete
    __public_key: Incomplete
    name: Incomplete
    asset: Incomplete
    _prv_keyfile: Incomplete
    _pub_keyfile: Incomplete
    def __init__(self, path: str, pub_keyfile: str | None = None, prv_keyfile: str | None = None, name: str | None = None, asset: AppriseAsset | None = None, **kwargs) -> None:
        """Path should be the directory keys can be written and read from such
        as <notifyobject>.store.path.

        Optionally additionally specify a keyfile to explicitly open
        """
    def load_private_key(self, path: str | None = None, *names: str) -> bool:
        """Load Private key and from that we can prepare our public key."""
    def load_public_key(self, path: str | None = None, *names: str) -> bool:
        """Load Public key only.

        Note: with just a public key you can only decrypt, encryption is not
              possible.
        """
    def keygen(self, name: str | None = None, force: bool = False):
        """Generates a set of keys based on name configured."""
    def public_keyfile(self, *names: str) -> str | None:
        """Returns the first match of a useable public key based names
        provided."""
    def private_keyfile(self, *names: str) -> str | None:
        """Returns the first match of a useable private key based names
        provided."""
    def public_key(self, *names: str, autogen: bool | None = None, autodetect: bool = True) -> ec.EllipticCurvePublicKey | None:
        """Opens a spcified pem public file and returns the key from it which
        is used to decrypt the message."""
    def private_key(self, *names: str, autogen: bool | None = None, autodetect: bool = True) -> ec.EllipticCurvePrivateKey | None:
        """Opens a spcified pem private file and returns the key from it which
        is used to encrypt the message."""
    def encrypt_webpush(self, message: str | bytes, public_key: ec.EllipticCurvePublicKey, auth_secret: bytes) -> bytes:
        """Encrypt a WebPush message using the recipient's public key and auth
        secret.

        Accepts input message as str or bytes.
        """
    def encrypt(self, message: str | bytes, public_key: ec.EllipticCurvePublicKey | None = None, salt: bytes | None = None) -> str | None:
        """Encrypts a message using the recipient's public key (or self public
        key if none provided).

        Message can be str or bytes.
        """
    def decrypt(self, encrypted_payload: str | bytes, private_key: ec.EllipticCurvePrivateKey | None = None, salt: bytes | None = None) -> str | None:
        """Decrypts a message using the provided private key or fallback to
        self's private key.

        Payload is the base64-encoded JSON from encrypt().
        """
    def sign(self, content: bytes) -> bytes | None:
        """Sign the message using ES256 (ECDSA w/ SHA256) via private key."""
    @property
    def pub_keyfile(self) -> str | bool | None:
        """Returns the Public Keyfile Path if set otherwise it returns None
        This property returns False if a keyfile was provided, but was
        invalid."""
    @property
    def prv_keyfile(self) -> str | bool | None:
        """Returns the Private Keyfile Path if set otherwise it returns None
        This property returns False if a keyfile was provided, but was
        invalid."""
    @property
    def x962_str(self) -> str:
        """X962 serialization based on public key."""
    def __bool__(self) -> bool:
        """Returns True if at least 1 key was loaded."""
