from ..common import NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from ..utils.base64 import decode_b64_dict as decode_b64_dict, encode_b64_dict as encode_b64_dict
from ..utils.parse import is_email as is_email, parse_bool as parse_bool, parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class OneSignalCategory:
    """We define the different category types that we can notify via
    OneSignal."""
    PLAYER: str
    EMAIL: str
    USER: str
    SEGMENT: str

ONESIGNAL_CATEGORIES: Incomplete

class NotifyOneSignal(NotifyBase):
    """A wrapper for OneSignal Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    image_size: Incomplete
    default_batch_size: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    template_kwargs: Incomplete
    apikey: Incomplete
    app: Incomplete
    batch_size: Incomplete
    use_contents: Incomplete
    decode_tpl_args: Incomplete
    include_image: Incomplete
    targets: Incomplete
    template_id: Incomplete
    subtitle: Incomplete
    language: Incomplete
    custom_data: Incomplete
    postback_data: Incomplete
    def __init__(self, app, apikey, targets=None, include_image: bool = True, template=None, subtitle=None, language=None, batch=None, use_contents=None, decode_tpl_args=None, custom=None, postback=None, **kwargs) -> None:
        """Initialize OneSignal."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform OneSignal Notification."""
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
