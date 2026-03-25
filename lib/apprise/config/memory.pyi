from .base import ConfigBase as ConfigBase
from _typeshed import Incomplete

class ConfigMemory(ConfigBase):
    """For information that was loaded from memory and does not persist
    anywhere."""
    service_name: Incomplete
    protocol: str
    content: Incomplete
    config_format: Incomplete
    def __init__(self, content, **kwargs) -> None:
        """Initialize Memory Object.

        Memory objects just store the raw configuration in memory.  There is no
        external reference point. It's always considered cached.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    def read(self, **kwargs):
        """Simply return content stored into memory."""
    @staticmethod
    def parse_url(url) -> None:
        """Memory objects have no parseable URL."""
