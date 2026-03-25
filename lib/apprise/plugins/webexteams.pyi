from ..common import NotifyFormat as NotifyFormat, NotifyType as NotifyType
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

WEBEX_HTTP_ERROR_MAP: Incomplete

class NotifyWebexTeams(NotifyBase):
    """A wrapper for Webex Teams Notifications."""
    service_name: str
    service_url: str
    secure_protocol: Incomplete
    setup_url: str
    notify_url: str
    body_maxlen: int
    title_maxlen: int
    notify_format: Incomplete
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    token: Incomplete
    def __init__(self, token, **kwargs) -> None:
        """Initialize Webex Teams Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Webex Teams Notification."""
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
    @staticmethod
    def parse_native_url(url):
        """
        Support https://api.ciscospark.com/v1/webhooks/incoming/WEBHOOK_TOKEN
        """
