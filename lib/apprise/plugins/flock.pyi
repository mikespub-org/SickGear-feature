from ..common import NotifyFormat as NotifyFormat, NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from ..utils.parse import parse_bool as parse_bool, parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

FLOCK_HTTP_ERROR_MAP: Incomplete
IS_CHANNEL_RE: Incomplete
IS_USER_RE: Incomplete

class NotifyFlock(NotifyBase):
    """A wrapper for Flock Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    notify_api: str
    image_size: Incomplete
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    targets: Incomplete
    token: Incomplete
    include_image: Incomplete
    def __init__(self, token, targets=None, include_image: bool = True, **kwargs) -> None:
        """Initialize Flock Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Flock Notification."""
    def _post(self, url, headers, payload):
        """A wrapper to the requests object."""
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
    @staticmethod
    def parse_native_url(url):
        """
        Support https://api.flock.com/hooks/sendMessage/TOKEN
        """
