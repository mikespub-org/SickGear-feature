from .. import exception as exception
from ..common import NotifyFormat as NotifyFormat, NotifyType as NotifyType, PersistentStoreMode as PersistentStoreMode
from ..conversion import convert_between as convert_between
from ..utils.parse import is_email as is_email, parse_emails as parse_emails, validate_regex as validate_regex
from ..utils.sanitize import sanitize_payload as sanitize_payload
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifySendPulse(NotifyBase):
    """
    A wrapper for Notify SendPulse Notifications
    """
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_format: Incomplete
    notify_email_url: str
    notify_oauth_url: str
    attachment_support: bool
    request_rate_per_sec: float
    storage_mode: Incomplete
    token_expiry: int
    token_expiry_edge: int
    default_empty_subject: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    template_kwargs: Incomplete
    names: Incomplete
    host: Incomplete
    from_addr: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    targets: Incomplete
    cc: Incomplete
    bcc: Incomplete
    template: Incomplete
    template_data: Incomplete
    def __init__(self, client_id, client_secret, from_addr=None, targets=None, cc=None, bcc=None, template=None, template_data=None, **kwargs) -> None:
        """
        Initialize Notify SendPulse Object
        """
    @property
    def url_identifier(self):
        """
        Returns all of the identifiers that make this URL unique from
        another simliar one. Targets or end points should never be identified
        here.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """
        Returns the URL built dynamically based on specified arguments.
        """
    def __len__(self) -> int:
        """
        Returns the number of targets associated with this notification
        """
    def login(self):
        """
        Authenticates with the server to get a access_token
        """
    def send(self, body, title: str = '', notify_type=..., attach=None, **kwargs):
        """
        Perform SendPulse Notification
        """
    def _fetch(self, url, payload, target=None, retry: int = 0):
        """
        Wrapper to request.post() to manage it's response better and make
        the send() function cleaner and easier to maintain.

        This function returns True if the _post was successful and False
        if it wasn't.
        """
    @staticmethod
    def parse_url(url):
        """
        Parses the URL and returns enough arguments that can allow
        us to re-instantiate this object.

        """
