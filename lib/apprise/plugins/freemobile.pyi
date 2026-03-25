from ..common import NotifyType as NotifyType
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyFreeMobile(NotifyBase):
    """A wrapper for Free-Mobile Notifications."""
    service_name: Incomplete
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    templates: Incomplete
    title_maxlen: int
    body_maxlen: int
    template_tokens: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize Free Mobile Object."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Send our notification."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
