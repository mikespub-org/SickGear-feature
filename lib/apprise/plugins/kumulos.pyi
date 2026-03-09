from ..common import NotifyType as NotifyType
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

KUMULOS_HTTP_ERROR_MAP: Incomplete

class NotifyKumulos(NotifyBase):
    """A wrapper for Kumulos Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    title_maxlen: int
    body_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    apikey: Incomplete
    serverkey: Incomplete
    def __init__(self, apikey, serverkey, **kwargs) -> None:
        """Initialize Kumulos Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Kumulos Notification."""
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
