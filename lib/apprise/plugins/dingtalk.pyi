from ..common import NotifyFormat as NotifyFormat, NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

IS_PHONE_NO: Incomplete

class NotifyDingTalk(NotifyBase):
    """A wrapper for DingTalk Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    token: Incomplete
    secret: Incomplete
    targets: Incomplete
    def __init__(self, token, targets=None, secret=None, **kwargs) -> None:
        """Initialize DingTalk Object."""
    def get_signature(self):
        """Calculates time-based signature so that we can send arbitrary
        messages."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform DingTalk Notification."""
    @property
    def title_maxlen(self):
        """The title isn't used when not in markdown mode."""
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def __len__(self) -> int:
        """Returns the number of targets associated with this notification."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to
        substantiate this object."""
