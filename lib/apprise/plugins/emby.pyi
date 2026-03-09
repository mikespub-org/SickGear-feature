from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import parse_bool as parse_bool
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyEmby(NotifyBase):
    """A wrapper for Emby Notifications."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    setup_url: str
    emby_device_id: str
    emby_message_timeout_ms: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    schema: str
    access_token: Incomplete
    user_id: Incomplete
    modal: Incomplete
    port: Incomplete
    def __init__(self, modal: bool = False, **kwargs) -> None:
        """Initialize Emby Object."""
    def login(self, **kwargs):
        """Creates our authentication token and prepares our header."""
    def sessions(self, user_controlled: bool = True):
        """Acquire our Session Identifiers and store them in a dictionary
        indexed by the session id itself."""
    def logout(self, **kwargs):
        """Logs out of an already-authenticated session."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Emby Notification."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    @property
    def is_authenticated(self):
        """Returns True if we're authenticated and False if not."""
    @property
    def emby_auth_header(self):
        """Generates the X-Emby-Authorization header response based on whether
        we're authenticated or not."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
    def __del__(self) -> None:
        """Destructor."""
