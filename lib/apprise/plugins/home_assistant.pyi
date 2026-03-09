from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyHomeAssistant(NotifyBase):
    """A wrapper for Home Assistant Notifications."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    default_insecure_port: int
    setup_url: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    fullpath: Incomplete
    port: Incomplete
    accesstoken: Incomplete
    nid: Incomplete
    def __init__(self, accesstoken, nid=None, **kwargs) -> None:
        """Initialize Home Assistant Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Sends Message."""
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
