from ..common import NotifyFormat as NotifyFormat, NotifyType as NotifyType
from ..utils.parse import parse_bool as parse_bool, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyPushMe(NotifyBase):
    """A wrapper for PushMe Notifications."""
    service_name: str
    service_url: str
    protocol: str
    setup_url: str
    notify_url: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    token: Incomplete
    status: Incomplete
    def __init__(self, token, status=None, **kwargs) -> None:
        """Initialize PushMe Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform PushMe Notification."""
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
