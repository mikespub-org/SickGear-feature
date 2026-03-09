from ..common import NotifyFormat as NotifyFormat, NotifyImageSize as NotifyImageSize, NotifyType as NotifyType, PersistentStoreMode as PersistentStoreMode
from ..exception import AppriseException as AppriseException
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import is_hostname as is_hostname, parse_bool as parse_bool, parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

MATRIX_V1_WEBHOOK_PATH: str
MATRIX_V2_API_PATH: str
MATRIX_V3_API_PATH: str
MATRIX_V3_MEDIA_PATH: str
MATRIX_V2_MEDIA_PATH: str

class MatrixDiscoveryException(AppriseException):
    """Apprise Matrix Exception Class."""

MATRIX_HTTP_ERROR_MAP: Incomplete
IS_ROOM_ALIAS: Incomplete
IS_ROOM_ID: Incomplete
IS_IMAGE: Incomplete

class MatrixMessageType:
    """The Matrix Message types."""
    TEXT: str
    NOTICE: str

MATRIX_MESSAGE_TYPES: Incomplete

class MatrixVersion:
    V2: str
    V3: str

MATRIX_VERSIONS: Incomplete

class MatrixWebhookMode:
    DISABLED: str
    MATRIX: str
    SLACK: str
    T2BOT: str

MATRIX_WEBHOOK_MODES: Incomplete

class NotifyMatrix(NotifyBase):
    """A wrapper for Matrix Notifications."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    attachment_support: bool
    setup_url: str
    image_size: Incomplete
    body_maxlen: int
    request_rate_per_sec: float
    default_retries: int
    default_wait_ms: int
    storage_mode: Incomplete
    default_cache_expiry_sec: Incomplete
    discovery_base_key: str
    discovery_identity_key: str
    discovery_cache_length_sec: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    rooms: Incomplete
    home_server: Incomplete
    user_id: Incomplete
    access_token: Incomplete
    transaction_id: int
    include_image: Incomplete
    discovery: Incomplete
    hsreq: Incomplete
    mode: Incomplete
    version: Incomplete
    msgtype: Incomplete
    def __init__(self, targets=None, mode=None, msgtype=None, version=None, include_image=None, discovery=None, hsreq=None, **kwargs) -> None:
        """Initialize Matrix Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Matrix Notification."""
    def _send_webhook_notification(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Matrix Notification as a webhook."""
    _re_slack_formatting_map: Incomplete
    _re_slack_formatting_rules: Incomplete
    def _slack_webhook_payload(self, body, title: str = '', notify_type=..., **kwargs):
        """Format the payload for a Slack based message."""
    def _matrix_webhook_payload(self, body, title: str = '', notify_type=..., **kwargs):
        """Format the payload for a Matrix based message."""
    def _t2bot_webhook_payload(self, body, title: str = '', notify_type=..., **kwargs):
        """Format the payload for a T2Bot Matrix based messages."""
    def _send_server_notification(self, body, title: str = '', notify_type=..., attach=None, **kwargs):
        """Perform Direct Matrix Server Notification (no webhook)"""
    def _send_attachments(self, attach):
        """Posts all of the provided attachments."""
    def _register(self):
        """Register with the service if possible."""
    def _login(self):
        """Acquires the matrix token required for making future requests.

        If we fail we return False, otherwise we return True
        """
    def _logout(self):
        """Relinquishes token from remote server."""
    def _room_join(self, room):
        """Joins a matrix room if we're not already in it.

        Otherwise it attempts to create it if it doesn't exist and always
        returns the room_id if it was successful, otherwise it returns None
        """
    def _room_create(self, room):
        """Creates a matrix room and return it's room_id if successful
        otherwise None is returned."""
    def _joined_rooms(self):
        """Returns a list of the current rooms the logged in user is a part
        of."""
    def _room_id(self, room):
        """Get room id from its alias.
        Args:
            room (str): The room alias name.

        Returns:
            returns the room id if it can, otherwise it returns None
        """
    def _fetch(self, path, payload=None, params=None, attachment=None, method: str = 'POST', url_override=None):
        """Wrapper to request.post() to manage it's response better and make
        the send() function cleaner and easier to maintain.

        This function always returns a 3-tuple:
            (success, response, status_code)

        The response is a dict when JSON is parseable, otherwise an empty dict.
        The status_code defaults to 500 on local failures.
        """
    def __del__(self) -> None:
        """Ensure we relinquish our token."""
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
        Support https://webhooks.t2bot.io/api/v1/matrix/hook/WEBHOOK_TOKEN/
        """
    def server_discovery(self):
        """
        Home Server Discovery as documented here:
           https://spec.matrix.org/v1.11/client-server-api/#well-known-uri
        """
    @property
    def base_url(self):
        """Returns the base_url if known."""
    @property
    def identity_url(self):
        """Returns the identity_url if known."""
