from ..common import NotifyType as NotifyType
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class ProwlPriority:
    LOW: int
    MODERATE: int
    NORMAL: int
    HIGH: int
    EMERGENCY: int

PROWL_PRIORITIES: Incomplete
PROWL_PRIORITY_MAP: Incomplete
PROWL_HTTP_ERROR_MAP: Incomplete

class NotifyProwl(NotifyBase):
    """A wrapper for Prowl Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    request_rate_per_sec: int
    body_maxlen: int
    title_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    priority: Incomplete
    apikey: Incomplete
    providerkey: Incomplete
    def __init__(self, apikey, providerkey=None, priority=None, **kwargs) -> None:
        """Initialize Prowl Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Prowl Notification."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
