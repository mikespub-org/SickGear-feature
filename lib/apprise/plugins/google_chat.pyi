from ..common import NotifyFormat as NotifyFormat, NotifyType as NotifyType
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyGoogleChat(NotifyBase):
    """A wrapper to Google Chat Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    notify_format: Incomplete
    title_maxlen: int
    body_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    workspace: Incomplete
    webhook_key: Incomplete
    webhook_token: Incomplete
    thread_key: Incomplete
    def __init__(self, workspace, webhook_key, webhook_token, thread_key=None, **kwargs) -> None:
        """Initialize Google Chat Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Google Chat Notification."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object.

        Syntax:
          gchat://workspace/webhook_key/webhook_token
          gchat://workspace/webhook_key/webhook_token/thread_key
        """
    @staticmethod
    def parse_native_url(url):
        """
        Support
           https://chat.googleapis.com/v1/spaces/{workspace}/messages
                 '?key={key}&token={token}
           https://chat.googleapis.com/v1/spaces/{workspace}/messages
                 '?key={key}&token={token}&threadKey={thread}
        """
