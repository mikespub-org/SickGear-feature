from .. import exception as exception
from ..common import NotifyFormat as NotifyFormat, NotifyType as NotifyType, PersistentStoreMode as PersistentStoreMode
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import is_email as is_email, parse_emails as parse_emails, validate_regex as validate_regex
from ..utils.sanitize import sanitize_payload as sanitize_payload
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyOffice365(NotifyBase):
    """A wrapper for Office 365 Notifications."""
    service_name: str
    service_url: str
    secure_protocol: Incomplete
    request_rate_per_sec: float
    setup_url: str
    graph_url: str
    auth_url: str
    attachment_support: bool
    storage_mode: Incomplete
    outlook_attachment_inline_max: int
    scope: str
    notify_format: Incomplete
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    tenant: Incomplete
    source: Incomplete
    client_id: Incomplete
    secret: Incomplete
    names: Incomplete
    cc: Incomplete
    bcc: Incomplete
    targets: Incomplete
    token: Incomplete
    token_expiry: Incomplete
    from_email: Incomplete
    from_name: Incomplete
    def __init__(self, tenant, client_id, secret, source=None, targets=None, cc=None, bcc=None, **kwargs) -> None:
        """Initialize Office 365 Object."""
    def send(self, body, title: str = '', notify_type=..., attach=None, **kwargs):
        """Perform Office 365 Notification."""
    def upload_attachment(self, attachment, message_id, name=None):
        """Uploads an attachment to a session."""
    def authenticate(self):
        """Logs into and acquires us an authentication token to work with."""
    def _fetch(self, url, payload=None, headers=None, content_type: str = 'application/json', method: str = 'POST'):
        """Wrapper to request object."""
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
