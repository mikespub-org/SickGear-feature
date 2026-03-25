from ..attachment.base import AttachBase as AttachBase
from ..common import NotifyType as NotifyType
from ..utils.parse import is_email as is_email, parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

PUSHBULLET_SEND_TO_ALL: str
PUSHBULLET_HTTP_ERROR_MAP: Incomplete

class NotifyPushBullet(NotifyBase):
    """A wrapper for PushBullet Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    request_rate_per_sec: float
    setup_url: str
    notify_url: str
    attachment_support: bool
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    accesstoken: Incomplete
    targets: Incomplete
    def __init__(self, accesstoken, targets=None, **kwargs) -> None:
        """Initialize PushBullet Object."""
    def send(self, body, title: str = '', notify_type=..., attach=None, **kwargs):
        """Perform PushBullet Notification."""
    def _send(self, url, payload, **kwargs):
        """Wrapper to the requests (post) object."""
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
