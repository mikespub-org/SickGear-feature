from ..common import NotifyFormat as NotifyFormat, NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import is_email as is_email, parse_list as parse_list
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

IS_CHANNEL: Incomplete
IS_CHANNEL_ID: Incomplete
LIST_DELIM: Incomplete

class NotifyTwist(NotifyBase):
    """A wrapper for Notify Twist Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    body_maxlen: int
    notify_format: Incomplete
    api_url: str
    request_rate_per_sec: float
    default_notification_channel: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    channels: Incomplete
    channel_ids: Incomplete
    token: Incomplete
    default_workspace: Incomplete
    _cached_workspaces: Incomplete
    _cached_channels: Incomplete
    email: Incomplete
    user: Incomplete
    host: Incomplete
    def __init__(self, email=None, targets=None, **kwargs) -> None:
        """Initialize Notify Twist Object."""
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
    def login(self):
        """A simple wrapper to authenticate with the Twist Server."""
    def logout(self):
        """A simple wrapper to log out of the server."""
    def get_workspaces(self):
        """Returns all workspaces associated with this user account as a set.

        This returned object is either an empty dictionary or one that
        looks like this:
           {
             'workspace': <workspace_id>,
             'workspace': <workspace_id>,
             'workspace': <workspace_id>,
           }

        All workspaces are made lowercase for comparison purposes
        """
    def get_channels(self, wid):
        """Simply returns the channel objects associated with the specified
        workspace id.

        This returned object is either an empty dictionary or one that
        looks like this:
           {
             'channel1': <channel_id>,
             'channel2': <channel_id>,
             'channel3': <channel_id>,
           }

        All channels are made lowercase for comparison purposes
        """
    def _channel_migration(self):
        """A simple wrapper to get all of the current workspaces including the
        default one.  This plays a role in what channel(s) get notified and
        where.

        A cache lookup has overhead, and is only required to be preformed if
        the user specified channels by their string value
        """
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Twist Notification."""
    def _fetch(self, url, payload=None, method: str = 'POST', login: bool = False):
        """Wrapper to Twist API requests object."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
    def __del__(self) -> None:
        """Destructor."""
