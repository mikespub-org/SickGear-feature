from ..common import NotifyType as NotifyType
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyWeComBot(NotifyBase):
    """A wrapper for WeCom Bot Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    templates: Incomplete
    title_maxlen: int
    template_tokens: Incomplete
    template_args: Incomplete
    key: Incomplete
    api_url: Incomplete
    def __init__(self, key, **kwargs) -> None:
        """Initialize WeCom Bot Object."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Wrapper to _send since we can alert more then one channel."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
    @staticmethod
    def parse_native_url(url):
        """
        Support https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=BOTKEY
        """
