from .. import __version__ as __version__
from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import is_call_sign as is_call_sign, parse_call_sign as parse_call_sign
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

APRS_LOCALES: Incomplete
APRS_BAD_CHARMAP: Incomplete
APRS_COMPILED_MAP: Incomplete

class NotifyAprs(NotifyBase):
    """A wrapper for APRS Notifications via APRS-IS."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_port: int
    body_maxlen: int
    device_id: str
    title_maxlen: int
    request_rate_per_sec: float
    aprs_encoding: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    sock: Incomplete
    targets: Incomplete
    user: Incomplete
    delay: Incomplete
    locale: Incomplete
    invalid_targets: Incomplete
    def __init__(self, targets=None, locale=None, delay=None, **kwargs) -> None:
        """Initialize APRS Object."""
    def socket_close(self) -> None:
        """Closes the socket connection whereas present."""
    def socket_open(self):
        """Establishes the connection to the APRS-IS socket server."""
    def aprsis_login(self):
        """Generate the APRS-IS login string, send it to the server and parse
        the response.

        Returns True/False wrt whether the login was successful
        """
    def socket_send(self, tx_data):
        '''Generic "Send data to a socket".'''
    def socket_reset(self):
        """Resets the socket's buffer."""
    def socket_receive(self, rx_len):
        '''Generic "Receive data from a socket".'''
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform APRS Notification."""
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
    def __del__(self) -> None:
        """Ensure we close any lingering connections."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
