from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import is_phone_no as is_phone_no, parse_phone_no as parse_phone_no, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

MODE_DETECT_RE: Incomplete

class TwilioNotificationMethod:
    """Twilio Notification Method."""
    SMS: str
    CALL: str

TWILIO_NOTIFICATION_METHODS: Incomplete

class TwilioMessageMode:
    """Twilio Message Mode."""
    TEXT: str
    WHATSAPP: str

class NotifyTwilio(NotifyBase):
    """A wrapper for Twilio Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    request_rate_per_sec: float
    validity_period: int
    setup_url: str
    notify_sms_url: str
    notify_call_url: str
    body_sms_maxlen: int
    body_call_maxlen: int
    title_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    account_sid: Incomplete
    auth_token: Incomplete
    apikey: Incomplete
    method: Incomplete
    default_mode: Incomplete
    source: Incomplete
    targets: Incomplete
    def __init__(self, account_sid, auth_token, source, targets=None, apikey=None, method=None, **kwargs) -> None:
        """Initialize Twilio Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Twilio Notification."""
    @property
    def body_maxlen(self):
        """The maximum allowable characters allowed in the body per message.
        It is dependent on the notification method."""
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
