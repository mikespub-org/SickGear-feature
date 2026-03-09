from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyPushjet(NotifyBase):
    """A wrapper for Pushjet Notifications."""
    service_name: str
    protocol: str
    secure_protocol: str
    setup_url: str
    request_rate_per_sec: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    secret_key: Incomplete
    def __init__(self, secret_key, **kwargs) -> None:
        """Initialize Pushjet Object."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Pushjet Notification."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object.

        Syntax:
           pjet://hostname/secret_key
           pjet://hostname:port/secret_key
           pjet://user:pass@hostname/secret_key
           pjet://user:pass@hostname:port/secret_key
           pjets://hostname/secret_key
           pjets://hostname:port/secret_key
           pjets://user:pass@hostname/secret_key
           pjets://user:pass@hostname:port/secret_key
        """
