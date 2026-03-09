from ..common import NotifyType as NotifyType
from ..utils.parse import is_phone_no as is_phone_no, parse_bool as parse_bool, parse_phone_no as parse_phone_no
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifySeven(NotifyBase):
    """A wrapper for seven Notifications."""
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
    apikey: Incomplete
    source: Incomplete
    flash: Incomplete
    label: Incomplete
    targets: Incomplete
    def __init__(self, apikey, targets=None, source=None, flash=None, label=None, **kwargs) -> None:
        """Initialize Seven Object."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another similar one.

        Targets or end points should never be identified here.
        """
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform seven Notification."""
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    def __len__(self) -> int:
        """Returns the number of targets associated with this notification."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
