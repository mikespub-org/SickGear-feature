from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyLark(NotifyBase):
    """A wrapper for Lark (Feishu) Notifications via Webhook."""
    service_name: Incomplete
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    templates: Incomplete
    template_tokens: Incomplete
    token: Incomplete
    webhook_url: Incomplete
    def __init__(self, token, **kwargs) -> None:
        """Initialize Email Object.

        The smtp_host and secure_mode can be automatically detected depending
        on how the URL was built
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Returns all of the identifiers that make this URL unique from
        another similar one.

        Targets or end points should never be identified here.
        """
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another similar one.

        Targets or end points should never be identified here.
        """
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
    @staticmethod
    def parse_native_url(url):
        """
        Support https://open.larksuite.com/open-apis/bot/v2/hook//WEBHOOK_TOKEN
        """
