from ..common import NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from ..utils.parse import parse_bool as parse_bool
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

NOTIFY_MACOSX_SUPPORT_ENABLED: bool
major: Incomplete
minor: Incomplete

class NotifyMacOSX(NotifyBase):
    """A wrapper for the MacOS X terminal-notifier tool.

    Source: https://github.com/julienXX/terminal-notifier
    """
    enabled = NOTIFY_MACOSX_SUPPORT_ENABLED
    requirements: Incomplete
    service_name: Incomplete
    service_url: str
    protocol: str
    setup_url: str
    image_size: Incomplete
    request_rate_per_sec: int
    body_max_line_count: int
    url_identifier: bool
    notify_paths: Incomplete
    templates: Incomplete
    template_args: Incomplete
    include_image: Incomplete
    notify_path: Incomplete
    click: Incomplete
    sound: Incomplete
    def __init__(self, sound=None, include_image: bool = True, click=None, **kwargs) -> None:
        """Initialize MacOSX Object."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform MacOSX Notification."""
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    @staticmethod
    def parse_url(url):
        """There are no parameters nessisary for this protocol; simply having
        gnome:// is all you need.

        This function just makes sure that is in place.
        """
