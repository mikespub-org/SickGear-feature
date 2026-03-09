from ..common import NotifyType as NotifyType
from ..utils.parse import is_phone_no as is_phone_no, parse_bool as parse_bool, parse_phone_no as parse_phone_no, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

D7NETWORKS_HTTP_ERROR_MAP: Incomplete

class NotifyD7Networks(NotifyBase):
    """A wrapper for D7 Networks Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    request_rate_per_sec: float
    setup_url: str
    notify_url: str
    body_maxlen: int
    title_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    batch: Incomplete
    source: Incomplete
    unicode: Incomplete
    token: Incomplete
    targets: Incomplete
    def __init__(self, token=None, targets=None, source=None, batch: bool = False, unicode=None, **kwargs) -> None:
        """Initialize D7 Networks Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Depending on whether we are set to batch mode or single mode this
        redirects to the appropriate handling."""
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def __len__(self) -> int:
        """Returns the number of targets associated with this notification."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
