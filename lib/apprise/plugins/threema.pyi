from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import is_email as is_email, is_phone_no as is_phone_no, parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class ThreemaRecipientTypes:
    """The supported recipient specifiers."""
    THREEMA_ID: str
    PHONE: str
    EMAIL: str

class NotifyThreema(NotifyBase):
    """A wrapper for Threema Gateway Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    body_maxlen: int
    title_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    secret: Incomplete
    targets: Incomplete
    invalid_targets: Incomplete
    def __init__(self, secret=None, targets=None, **kwargs) -> None:
        """Initialize Threema Gateway Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Threema Gateway Notification."""
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
