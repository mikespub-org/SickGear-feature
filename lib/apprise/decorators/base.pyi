from .. import common as common
from ..logger import logger as logger
from ..manager_plugins import NotificationManager as NotificationManager
from ..plugins.base import NotifyBase as NotifyBase
from ..utils.logic import dict_full_update as dict_full_update
from ..utils.parse import URL_DETAILS_RE as URL_DETAILS_RE, parse_url as parse_url, url_assembly as url_assembly
from _typeshed import Incomplete

N_MGR: Incomplete

class CustomNotifyPlugin(NotifyBase):
    """Apprise Custom Plugin Hook.

    This gets initialized based on @notify decorator definitions
    """
    service_url: str
    category: str
    attachment_support: bool
    storage_mode: Incomplete
    templates: Incomplete
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns arguments retrieved."""
    def url(self, privacy: bool = False, *args, **kwargs):
        """General URL assembly."""
    _default_args: Incomplete
    @staticmethod
    def instantiate_plugin(url, send_func, name=None):
        """The function used to add a new notification plugin based on the
        schema parsed from the provided URL into our supported matrix
        structure."""
