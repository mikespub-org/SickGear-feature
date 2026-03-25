from .. import exception as exception
from ..common import NotifyType as NotifyType
from ..utils.parse import parse_list as parse_list, validate_regex as validate_regex
from ..utils.sanitize import sanitize_payload as sanitize_payload
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class PushSaferSound:
    """Defines all of the supported PushSafe sounds."""
    SILENT: int
    AHEM: int
    APPLAUSE: int
    ARROW: int
    BABY: int
    BELL: int
    BICYCLE: int
    BOING: int
    BUZZER: int
    CAMERA: int
    CAR_HORN: int
    CASH_REGISTER: int
    CHIME: int
    CREAKY_DOOR: int
    CUCKOO_CLOCK: int
    DISCONNECT: int
    DOG: int
    DOORBELL: int
    FANFARE: int
    GUN_SHOT: int
    HONK: int
    JAW_HARP: int
    MORSE: int
    ELECTRICITY: int
    RADIO_TURNER: int
    SIRENS: int
    MILITARY_TRUMPETS: int
    UFO: int
    LONG_WHAH: int
    GOODBYE: int
    HELLO: int
    NO: int
    OKAY: int
    OOOHHHWEEE: int
    WARNING: int
    WELCOME: int
    YEAH: int
    YES: int
    BEEP1: int
    WEEE: int
    CUTINOUT: int
    FLICK_GLASS: int
    SHORT_WHAH: int
    LASER: int
    WIND_CHIME: int
    ECHO: int
    ZIPPER: int
    HIHAT: int
    BEEP2: int
    BEEP3: int
    BEEP4: int
    ALARM_ARMED: int
    ALARM_DISARMED: int
    BACKUP_READY: int
    DOOR_CLOSED: int
    DOOR_OPENED: int
    WINDOW_CLOSED: int
    WINDOW_OPEN: int
    LIGHT_ON: int
    LIGHT_OFF: int
    DOORBELL_RANG: int

PUSHSAFER_SOUND_MAP: Incomplete

class PushSaferPriority:
    LOW: int
    MODERATE: int
    NORMAL: int
    HIGH: int
    EMERGENCY: int

PUSHSAFER_PRIORITIES: Incomplete
PUSHSAFER_PRIORITY_MAP: Incomplete
DEFAULT_PRIORITY: str

class PushSaferVibration:
    """Defines the acceptable vibration settings for notification."""
    LOW: int
    NORMAL: int
    HIGH: int

PUSHSAFER_VIBRATIONS: Incomplete
PICTURE_PARAMETER: Incomplete
PUSHSAFER_SEND_TO_ALL: str

class NotifyPushSafer(NotifyBase):
    """A wrapper for PushSafer Notifications."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    attachment_support: bool
    request_rate_per_sec: float
    default_pushsafer_icon: int
    setup_url: str
    notify_url: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    priority: Incomplete
    sound: Incomplete
    vibration: Incomplete
    privatekey: Incomplete
    targets: Incomplete
    def __init__(self, privatekey, targets=None, priority=None, sound=None, vibration=None, **kwargs) -> None:
        """Initialize PushSafer Object."""
    def send(self, body, title: str = '', notify_type=..., attach=None, **kwargs):
        """Perform PushSafer Notification."""
    def _send(self, payload, **kwargs):
        """Wrapper to the requests (post) object."""
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
