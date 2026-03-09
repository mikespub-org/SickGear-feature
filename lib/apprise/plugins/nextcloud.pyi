from ..common import NotifyType as NotifyType, PersistentStoreMode as PersistentStoreMode
from ..exception import AppriseException as AppriseException
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import parse_list as parse_list
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

IS_GROUP: Incomplete
IS_USER: Incomplete

class NextcloudGroupDiscoveryException(AppriseException):
    """Apprise Nextcloud Group Discovery Exception Class."""

class NotifyNextcloud(NotifyBase):
    """A wrapper for Nextcloud Notifications.

    Targets can be individual users, groups, or everyone:
    - user: specify one or more usernames as path segments
    - group: prefix with a hash (e.g., ``#DevTeam``)
    - everyone: use ``all`` (aliases: ``everyone``, ``*``)

    Group and everyone expansion uses Nextcloud's OCS provisioning API and
    requires appropriate permissions (typically an admin account) and the
    provisioning API enabled on the server.
    """
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    setup_url: str
    title_maxlen: int
    body_maxlen: int
    storage_mode: Incomplete
    group_discovery_cache_length_sec: int
    all_group_id: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    template_kwargs: Incomplete
    targets: Incomplete
    groups: Incomplete
    version: Incomplete
    url_prefix: Incomplete
    headers: Incomplete
    def __init__(self, targets=None, version=None, headers=None, url_prefix=None, **kwargs) -> None:
        """Initialize Nextcloud Object."""
    def _fetch(self, payload=None, target=None, group=None):
        """Wrapper to NextCloud API requests object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Nextcloud Notification."""
    def users_by_group(self, group):
        """
        Lists users associated with a provided group
        """
    def all_users(self):
        """
        Lists users associated with Nextcloud instance
        """
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
