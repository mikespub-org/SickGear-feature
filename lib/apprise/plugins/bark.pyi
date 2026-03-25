from ..common import NotifyFormat as NotifyFormat, NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import parse_bool as parse_bool, parse_list as parse_list
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

BARK_SOUNDS: Incomplete

class NotifyBarkLevel:
    """Defines the Bark Level options."""
    ACTIVE: str
    TIME_SENSITIVE: str
    PASSIVE: str
    CRITICAL: str

BARK_LEVELS: Incomplete

class NotifyBark(NotifyBase):
    """A wrapper for Notify Bark Notifications."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    setup_url: str
    image_size: Incomplete
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    notify_url: Incomplete
    category: Incomplete
    group: Incomplete
    targets: Incomplete
    include_image: Incomplete
    click: Incomplete
    badge: Incomplete
    sound: Incomplete
    volume: Incomplete
    call: Incomplete
    icon: Incomplete
    level: Incomplete
    def __init__(self, targets=None, include_image: bool = True, sound=None, category=None, group=None, level=None, click=None, badge=None, volume=None, icon=None, call=None, **kwargs) -> None:
        """Initialize Notify Bark Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Bark Notification."""
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
