from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import is_phone_no as is_phone_no, parse_bool as parse_bool, parse_phone_no as parse_phone_no, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class BurstSMSCountryCode:
    AU: str
    NZ: str
    UK: str
    US: str

BURST_SMS_COUNTRY_CODES: Incomplete

class NotifyBurstSMS(NotifyBase):
    """A wrapper for Burst SMS Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    default_batch_size: int
    setup_url: str
    notify_url: str
    body_maxlen: int
    title_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    apikey: Incomplete
    secret: Incomplete
    country: Incomplete
    validity: Incomplete
    batch: Incomplete
    source: Incomplete
    targets: Incomplete
    def __init__(self, apikey, secret, source, targets=None, country=None, validity=None, batch=None, **kwargs) -> None:
        """Initialize Burst SMS Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Burst SMS Notification."""
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
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
