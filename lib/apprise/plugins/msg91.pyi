from ..common import NotifyType as NotifyType
from ..utils.parse import is_phone_no as is_phone_no, parse_bool as parse_bool, parse_phone_no as parse_phone_no, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class MSG91PayloadField:
    """Identifies the fields available in the JSON Payload."""
    BODY: str
    MESSAGETYPE: str

RESERVED_KEYWORDS: Incomplete

class NotifyMSG91(NotifyBase):
    """A wrapper for MSG91 Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    body_maxlen: int
    title_maxlen: int
    component_key_re: Incomplete
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    template_kwargs: Incomplete
    authkey: Incomplete
    template: Incomplete
    short_url: Incomplete
    targets: Incomplete
    template_mapping: Incomplete
    def __init__(self, template, authkey, targets=None, short_url=None, template_mapping=None, **kwargs) -> None:
        """Initialize MSG91 Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform MSG91 Notification."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    def __len__(self) -> int:
        """Returns the number of targets associated with this notification."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
