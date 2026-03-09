from ..common import ConfigFormat as ConfigFormat, ContentIncludeMode as ContentIncludeMode
from ..utils.disk import path_decode as path_decode
from .base import ConfigBase as ConfigBase
from _typeshed import Incomplete

class ConfigFile(ConfigBase):
    """A wrapper for File based configuration sources."""
    service_name: Incomplete
    protocol: str
    allow_cross_includes: Incomplete
    path: Incomplete
    __original_path: Incomplete
    config_path: Incomplete
    def __init__(self, path, **kwargs) -> None:
        """Initialize File Object.

        headers can be a dictionary of key/value pairs that you want to
        additionally include as part of the server headers to post with
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    def read(self, **kwargs):
        """Perform retrieval of the configuration based on the specified
        request."""
    @staticmethod
    def parse_url(url):
        """Parses the URL so that we can handle all different file paths and
        return it as our path object."""
