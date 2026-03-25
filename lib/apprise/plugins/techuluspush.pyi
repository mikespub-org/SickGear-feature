from ..common import NotifyType as NotifyType
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

UUID4_RE: str

class NotifyTechulusPush(NotifyBase):
    """A wrapper for Techulus Push Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    body_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    apikey: Incomplete
    def __init__(self, apikey, **kwargs) -> None:
        """Initialize Techulus Push Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Techulus Push Notification."""
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
