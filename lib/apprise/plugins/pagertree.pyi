from ..common import NotifyType as NotifyType
from ..utils.parse import parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class PagerTreeAction:
    CREATE: str
    ACKNOWLEDGE: str
    RESOLVE: str

class PagerTreeUrgency:
    SILENT: str
    LOW: str
    MEDIUM: str
    HIGH: str
    CRITICAL: str

PAGERTREE_ACTIONS: Incomplete
PAGERTREE_URGENCIES: Incomplete
PAGERTREE_HTTP_ERROR_MAP: Incomplete

class NotifyPagerTree(NotifyBase):
    """A wrapper for PagerTree Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    template_kwargs: Incomplete
    integration: Incomplete
    thirdparty: Incomplete
    headers: Incomplete
    payload_extras: Incomplete
    meta_extras: Incomplete
    action: Incomplete
    urgency: Incomplete
    __tags: Incomplete
    def __init__(self, integration, action=None, thirdparty=None, urgency=None, tags=None, headers=None, payload_extras=None, meta_extras=None, **kwargs) -> None:
        """Initialize PagerTree Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform PagerTree Notification."""
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
