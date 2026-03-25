from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

IS_CHANNEL: Incomplete
IS_USER_PUSHED_ID: Incomplete

class NotifyPushed(NotifyBase):
    """A wrapper to Pushed Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    title_maxlen: int
    body_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    app_key: Incomplete
    app_secret: Incomplete
    channels: Incomplete
    users: Incomplete
    def __init__(self, app_key, app_secret, targets=None, **kwargs) -> None:
        """Initialize Pushed Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Pushed Notification."""
    def _send(self, payload, notify_type, **kwargs):
        """A lower level call that directly pushes a payload to the Pushed
        Notification servers.

        This should never be called directly; it is referenced automatically
        through the send() function.
        """
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
