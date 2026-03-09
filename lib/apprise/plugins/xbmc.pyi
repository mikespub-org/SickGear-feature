from ..common import NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import parse_bool as parse_bool
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyXBMC(NotifyBase):
    """A wrapper for XBMC/KODI Notifications."""
    service_name: str
    service_url: str
    xbmc_protocol: str
    xbmc_secure_protocol: str
    kodi_protocol: str
    kodi_secure_protocol: str
    protocol: Incomplete
    secure_protocol: Incomplete
    setup_url: str
    request_rate_per_sec: int
    body_max_line_count: int
    xbmc_default_port: int
    image_size: Incomplete
    xbmc_remote_protocol: int
    kodi_remote_protocol: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    duration: Incomplete
    schema: Incomplete
    headers: Incomplete
    include_image: Incomplete
    def __init__(self, include_image: bool = True, duration=None, **kwargs) -> None:
        """Initialize XBMC/KODI Object."""
    def _payload_60(self, title, body, notify_type, **kwargs):
        """Builds payload for KODI API v6.0.

        Returns (headers, payload)
        """
    def _payload_20(self, title, body, notify_type, **kwargs):
        """Builds payload for XBMC API v2.0.

        Returns (headers, payload)
        """
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform XBMC/KODI Notification."""
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
        instantiate this object."""
