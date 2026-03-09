from ..common import NotifyType as NotifyType
from ..utils.parse import is_email as is_email, is_phone_no as is_phone_no, parse_phone_no as parse_phone_no
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyVoipms(NotifyBase):
    """A wrapper for VoIPms Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    body_maxlen: int
    voip_ms_country_code: str
    title_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    email: Incomplete
    source: Incomplete
    targets: Incomplete
    def __init__(self, email, source=None, targets=None, **kwargs) -> None:
        """Initialize VoIPms Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform VoIPms Notification."""
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
