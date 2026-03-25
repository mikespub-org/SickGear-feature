from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyQQ(NotifyBase):
    """A wrapper for QQ Push Notifications."""
    service_name: Incomplete
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    templates: Incomplete
    template_tokens: Incomplete
    token: Incomplete
    webhook_url: Incomplete
    def __init__(self, token, **kwargs) -> None:
        """Initialize QQ Push Object.

        Args:
            token (str): User push token from QQ Push provider (e.g., Qmsg)
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    @property
    def url_identifier(self):
        """Returns a unique identifier for this plugin instance."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Send a QQ Push Notification."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns arguments to re-instantiate the
        object."""
    @staticmethod
    def parse_native_url(url):
        """Parse native QQ push-style URL into Apprise format."""
