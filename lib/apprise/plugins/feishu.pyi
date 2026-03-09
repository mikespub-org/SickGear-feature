from ..common import NotifyType as NotifyType
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyFeishu(NotifyBase):
    """A wrapper for Feishu Notifications."""
    service_name: Incomplete
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    templates: Incomplete
    title_maxlen: int
    body_maxlen: int
    template_tokens: Incomplete
    template_args: Incomplete
    token: Incomplete
    def __init__(self, token, **kwargs) -> None:
        """Initialize Feishu Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Send our notification."""
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
