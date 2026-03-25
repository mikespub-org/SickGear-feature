from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import parse_list as parse_list
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyNextcloudTalk(NotifyBase):
    """A wrapper for Nextcloud Talk Notifications."""
    service_name: Incomplete
    service_url: str
    protocol: str
    secure_protocol: str
    setup_url: str
    title_maxlen: int
    body_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    template_kwargs: Incomplete
    targets: Incomplete
    url_prefix: Incomplete
    headers: Incomplete
    def __init__(self, targets=None, headers=None, url_prefix=None, **kwargs) -> None:
        """Initialize Nextcloud Talk Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Nextcloud Talk Notification."""
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
