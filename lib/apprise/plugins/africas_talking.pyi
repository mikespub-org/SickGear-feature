from ..common import NotifyType as NotifyType
from ..utils.parse import is_phone_no as is_phone_no, parse_bool as parse_bool, parse_phone_no as parse_phone_no, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class AfricasTalkingSMSMode:
    """Africas Talking SMS Mode."""
    BULKSMS: str
    PREMIUM: str
    SANDBOX: str

AFRICAS_TALKING_SMS_MODES: Incomplete
AFRICAS_TALKING_HTTP_ERROR_MAP: Incomplete

class NotifyAfricasTalking(NotifyBase):
    """A wrapper for Africas Talking Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: Incomplete
    title_maxlen: int
    body_maxlen: int
    default_batch_size: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    appuser: Incomplete
    apikey: Incomplete
    sender: Incomplete
    batch: Incomplete
    mode: Incomplete
    targets: Incomplete
    def __init__(self, appuser, apikey, targets=None, sender=None, batch=None, mode=None, **kwargs) -> None:
        """Initialize Africas Talking Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Africas Talking Notification."""
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
