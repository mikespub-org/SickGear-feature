from ..common import NotifyType as NotifyType
from ..utils.parse import parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyIFTTT(NotifyBase):
    """A wrapper for IFTTT Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    ifttt_default_key_prefix: str
    ifttt_default_title_key: str
    ifttt_default_body_key: str
    ifttt_default_type_key: str
    notify_url: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    template_kwargs: Incomplete
    webhook_id: Incomplete
    events: Incomplete
    add_tokens: Incomplete
    del_tokens: Incomplete
    def __init__(self, webhook_id, events, add_tokens=None, del_tokens=None, **kwargs) -> None:
        """Initialize IFTTT Object.

        add_tokens can optionally be a dictionary of key/value pairs that you
        want to include in the IFTTT post to the server.

        del_tokens can optionally be a list/tuple/set of tokens that you want
        to eliminate from the IFTTT post.  There isn't much real functionality
        to this one unless you want to remove reference to Value1, Value2,
        and/or Value3
        """
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform IFTTT Notification."""
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
        Support https://maker.ifttt.com/use/WEBHOOK_ID/EVENT_ID
        """
