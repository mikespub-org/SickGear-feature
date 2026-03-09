from ...apprise_attachment import AppriseAttachment as AppriseAttachment
from ...asset import AppriseAsset as AppriseAsset
from ...exception import AppriseInvalidData as AppriseInvalidData
from ...utils.base64 import base64_urldecode as base64_urldecode
from _typeshed import Incomplete
from cryptography.hazmat.primitives.asymmetric import ec

CRYPTOGRAPHY_SUPPORT: bool

class WebPushSubscription:
    """WebPush Subscription."""
    __endpoint: Incomplete
    __p256dh: Incomplete
    __auth: Incomplete
    __auth_secret: Incomplete
    __public_key: Incomplete
    def __init__(self, content: str | dict | None = None) -> None:
        """Prepares a webpush object provided with content Content can be a
        dictionary, or JSON String."""
    def load(self, content: str | dict | None = None) -> bool:
        """Performs the loading/validation of the object."""
    def write(self, path: str, indent: int = 2) -> bool:
        """Writes content to disk based on path specified.

        Content is a JSON file, so ideally you may wish to have `.json' as it's
        extension for clarity
        """
    @property
    def auth(self) -> str | None: ...
    @property
    def endpoint(self) -> str | None: ...
    @property
    def p256dh(self) -> str | None: ...
    @property
    def auth_secret(self) -> bytes | None: ...
    @property
    def public_key(self) -> ec.EllipticCurvePublicKey | None: ...
    @property
    def dict(self) -> dict: ...
    def json(self, indent: int = 2) -> str:
        """Returns JSON representation of the object."""
    def __bool__(self) -> bool:
        """Handle 'if' statement."""
    def __str__(self) -> str:
        """Returns our JSON entry as a string."""

class WebPushSubscriptionManager:
    """WebPush Subscription Manager."""
    max_load_failure_count: int
    __subscriptions: Incomplete
    asset: Incomplete
    def __init__(self, asset: AppriseAsset | None = None) -> None:
        """Webpush Subscription Manager."""
    def __getitem__(self, key: str) -> WebPushSubscription:
        """Returns our indexed value if it exists."""
    def __setitem__(self, name: str, subscription: WebPushSubscription | str | dict) -> None:
        """Set's our object if possible."""
    def add(self, subscription: WebPushSubscription | str | dict, name: str | None = None) -> bool:
        """Add a subscription into our manager."""
    def __bool__(self) -> bool:
        """True is returned if at least one subscription has been loaded."""
    def __len__(self) -> int:
        """Returns the number of servers loaded; this includes those found
        within loaded configuration.

        This funtion nnever actually counts the Config entry themselves (if
        they exist), only what they contain.
        """
    def __iadd__(self, subscription: WebPushSubscription | str | dict) -> WebPushSubscriptionManager: ...
    def __contains__(self, key: str) -> bool:
        """Checks if the key exists."""
    def clear(self) -> None:
        """Empties our server list."""
    @property
    def dict(self) -> dict:
        """Returns a dictionary of all entries."""
    def load(self, path: str, byte_limit: int = 0) -> bool:
        """Writes content to disk based on path specified.  Content is a JSON
        file, so ideally you may wish to have `.json' as it's extension for
        clarity.

        if byte_limit is zero, then we do not limit our file size, otherwise
        set this to the bytes you want to restrict yourself by
        """
    def write(self, path: str, indent: int = 2) -> bool:
        """Writes content to disk based on path specified.

        Content is a JSON file, so ideally you may wish to have `.json' as it's
        extension for clarity
        """
    def json(self, indent: int = 2) -> str:
        """Returns JSON representation of the object."""
