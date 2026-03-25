from .. import exception as exception
from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import is_phone_no as is_phone_no, parse_bool as parse_bool, parse_phone_no as parse_phone_no
from ..utils.sanitize import sanitize_payload as sanitize_payload
from .base import NotifyBase as NotifyBase, NotifyFormat as NotifyFormat
from _typeshed import Incomplete

GROUP_REGEX: Incomplete

class NotifySignalAPI(NotifyBase):
    """A wrapper for SignalAPI Notifications."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    setup_url: str
    attachment_support: bool
    default_batch_size: int
    title_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    batch: Incomplete
    status: Incomplete
    targets: Incomplete
    invalid_targets: Incomplete
    source: Incomplete
    def __init__(self, source=None, targets=None, batch: bool = False, status: bool = False, **kwargs) -> None:
        """Initialize SignalAPI Object."""
    def send(self, body, title: str = '', notify_type=..., attach=None, **kwargs):
        """Perform Signal API Notification."""
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
