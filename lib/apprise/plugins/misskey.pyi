from ..common import NotifyType as NotifyType
from ..utils.parse import validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class MisskeyVisibility:
    """The visibility of any note created."""
    PUBLIC: str
    HOME: str
    FOLLOWERS: str
    SPECIFIED: str

MISSKEY_VISIBILITIES: Incomplete

class NotifyMisskey(NotifyBase):
    """A wrapper for Misskey Notifications."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    setup_url: str
    title_maxlen: int
    body_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    token: Incomplete
    visibility: Incomplete
    schema: Incomplete
    api_url: Incomplete
    def __init__(self, token=None, visibility=None, **kwargs) -> None:
        """Initialize Misskey Object."""
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
