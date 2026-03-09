from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifySpike(NotifyBase):
    """A wrapper for Spike.sh Notifications."""
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
        """Initialize Spike.sh Object."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Send Spike.sh Notification."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns arguments to re-instantiate the
        object."""
    @staticmethod
    def parse_native_url(url):
        """Supports reverse-parsing a Spike.sh native URL into an Apprise
        one."""
