from ..common import NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from ..utils.parse import parse_bool as parse_bool, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class RyverWebhookMode:
    """Ryver supports to webhook modes."""
    SLACK: str
    RYVER: str

RYVER_WEBHOOK_MODES: Incomplete

class NotifyRyver(NotifyBase):
    """A wrapper for Ryver Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    image_size: Incomplete
    body_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    token: Incomplete
    organization: Incomplete
    mode: Incomplete
    include_image: Incomplete
    _re_formatting_map: Incomplete
    _re_formatting_rules: Incomplete
    def __init__(self, organization, token, mode=..., include_image: bool = True, **kwargs) -> None:
        """Initialize Ryver Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Ryver Notification."""
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
        Support https://RYVER_ORG.ryver.com/application/webhook/TOKEN
        """
