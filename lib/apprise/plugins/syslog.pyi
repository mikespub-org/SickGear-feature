from ..common import NotifyType as NotifyType
from ..utils.parse import parse_bool as parse_bool
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class SyslogFacility:
    """All of the supported facilities."""
    KERN: str
    USER: str
    MAIL: str
    DAEMON: str
    AUTH: str
    SYSLOG: str
    LPR: str
    NEWS: str
    UUCP: str
    CRON: str
    LOCAL0: str
    LOCAL1: str
    LOCAL2: str
    LOCAL3: str
    LOCAL4: str
    LOCAL5: str
    LOCAL6: str
    LOCAL7: str

SYSLOG_FACILITY_MAP: Incomplete
SYSLOG_FACILITY_RMAP: Incomplete
SYSLOG_PUBLISH_MAP: Incomplete

class NotifySyslog(NotifyBase):
    """A wrapper for Syslog Notifications."""
    service_name: str
    service_url: str
    protocol: str
    setup_url: str
    url_identifier: bool
    request_rate_per_sec: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    facility: Incomplete
    logoptions: int
    log_pid: Incomplete
    log_perror: Incomplete
    def __init__(self, facility=None, log_pid: bool = True, log_perror: bool = False, **kwargs) -> None:
        """Initialize Syslog Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Syslog Notification."""
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
