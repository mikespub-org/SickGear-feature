from ..common import NotifyType as NotifyType
from ..utils.parse import parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

VALIDATE_DEVICE: Incomplete
VALIDATE_TOPIC: Incomplete
PUSHY_HTTP_ERROR_MAP: Incomplete

class NotifyPushy(NotifyBase):
    """A wrapper for Pushy Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    body_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    apikey: Incomplete
    devices: Incomplete
    topics: Incomplete
    sound: Incomplete
    badge: Incomplete
    def __init__(self, apikey, targets=None, sound=None, badge=None, **kwargs) -> None:
        """Initialize Pushy Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Pushy Notification."""
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
