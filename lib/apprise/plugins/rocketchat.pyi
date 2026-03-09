from ..common import NotifyFormat as NotifyFormat, NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import parse_bool as parse_bool, parse_list as parse_list
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

IS_CHANNEL: Incomplete
IS_USER: Incomplete
IS_ROOM_ID: Incomplete
RC_HTTP_ERROR_MAP: Incomplete

class RocketChatAuthMode:
    """The Chat Authentication mode is detected."""
    WEBHOOK: str
    TOKEN: str
    BASIC: str

ROCKETCHAT_AUTH_MODES: Incomplete

class NotifyRocketChat(NotifyBase):
    """A wrapper for Notify Rocket.Chat Notifications."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    setup_url: str
    image_size: Incomplete
    title_maxlen: int
    body_maxlen: int
    notify_format: Incomplete
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    schema: Incomplete
    api_url: Incomplete
    channels: Incomplete
    rooms: Incomplete
    users: Incomplete
    webhook: Incomplete
    headers: Incomplete
    mode: Incomplete
    avatar: Incomplete
    def __init__(self, webhook=None, targets=None, mode=None, avatar=None, **kwargs) -> None:
        """Initialize Notify Rocket.Chat Object."""
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
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Wrapper to _send since we can alert more then one channel."""
    def _send_webhook_notification(self, body, title: str = '', notify_type=..., **kwargs):
        """Sends a webhook notification."""
    def _send_basic_notification(self, body, title: str = '', notify_type=..., **kwargs):
        """Authenticates with the server using a user/pass combo for
        notifications."""
    def _payload(self, body, title: str = '', notify_type=...):
        """Prepares a payload object."""
    def _send(self, payload, notify_type, path: str = 'api/v1/chat.postMessage', **kwargs):
        """Perform Notify Rocket.Chat Notification."""
    def login(self):
        """Login to our server."""
    def logout(self):
        """Logout of our server."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
