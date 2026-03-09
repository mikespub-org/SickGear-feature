from ..common import NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import parse_bool as parse_bool, parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

TARGET_LIST_DELIM: Incomplete

class NotifyLine(NotifyBase):
    """A wrapper for Line Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    notify_url: str
    setup_url: str
    title_maxlen: int
    body_maxlen: int
    image_size: Incomplete
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    token: Incomplete
    include_image: Incomplete
    targets: Incomplete
    __cached_users: Incomplete
    def __init__(self, token, targets=None, include_image: bool = True, **kwargs) -> None:
        """Initialize Line Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Send our Line Notification."""
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
