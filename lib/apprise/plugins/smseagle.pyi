from .. import exception as exception
from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import is_phone_no as is_phone_no, parse_bool as parse_bool, parse_phone_no as parse_phone_no, validate_regex as validate_regex
from ..utils.sanitize import sanitize_payload as sanitize_payload
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

GROUP_REGEX: Incomplete
CONTACT_REGEX: Incomplete

class SMSEaglePriority:
    NORMAL: int
    HIGH: int

SMSEAGLE_PRIORITIES: Incomplete
SMSEAGLE_PRIORITY_MAP: Incomplete

class SMSEagleCategory:
    """We define the different category types that we can notify via SMS
    Eagle."""
    PHONE: str
    GROUP: str
    CONTACT: str

SMSEAGLE_CATEGORIES: Incomplete

class NotifySMSEagle(NotifyBase):
    """A wrapper for SMSEagle Notifications."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    setup_url: str
    notify_path: str
    attachment_support: bool
    body_maxlen: int
    default_batch_size: int
    title_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    flash: Incomplete
    test: Incomplete
    batch: Incomplete
    status: Incomplete
    target_phones: Incomplete
    target_groups: Incomplete
    target_contacts: Incomplete
    invalid_targets: Incomplete
    token: Incomplete
    priority: Incomplete
    def __init__(self, token=None, targets=None, priority=None, batch: bool = False, status: bool = False, flash: bool = False, test: bool = False, **kwargs) -> None:
        """Initialize SMSEagle Object."""
    def send(self, body, title: str = '', notify_type=..., attach=None, **kwargs):
        """Perform SMSEagle Notification."""
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
