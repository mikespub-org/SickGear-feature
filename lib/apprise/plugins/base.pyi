from ..apprise_attachment import AppriseAttachment as AppriseAttachment
from ..common import NOTIFY_FORMATS as NOTIFY_FORMATS, NotifyFormat as NotifyFormat, NotifyImageSize as NotifyImageSize, NotifyType as NotifyType, OVERFLOW_MODES as OVERFLOW_MODES, OverflowMode as OverflowMode, PersistentStoreMode as PersistentStoreMode
from ..locale import Translatable as Translatable
from ..persistent_store import PersistentStore as PersistentStore
from ..url import URLBase as URLBase
from ..utils.format import smart_split as smart_split
from ..utils.parse import parse_bool as parse_bool
from ..utils.time import zoneinfo as zoneinfo
from _typeshed import Incomplete
from collections.abc import Generator
from datetime import tzinfo
from typing import Any, ClassVar, TypedDict

class RequirementsSpec(TypedDict, total=False):
    """Defines our plugin requirements."""
    packages_required: str | list[str] | None
    packages_recommended: str | list[str] | None
    details: Translatable | None

class NotifyBase(URLBase):
    """This is the base class for all notification services."""
    enabled: bool
    category: str
    requirements: ClassVar[RequirementsSpec]
    service_url: Incomplete
    setup_url: Incomplete
    request_rate_per_sec: float
    image_size: Incomplete
    body_maxlen: int
    title_maxlen: int
    body_max_line_count: int
    persistent_storage: bool
    timezone: Incomplete
    notify_format: Incomplete
    overflow_mode: Incomplete
    storage_mode: Incomplete
    interpret_emojis: bool
    attachment_support: bool
    default_html_tag_id: str
    template_args: Incomplete
    overflow_max_display_count_width: int
    overflow_buffer: int
    overflow_display_count_threshold: int
    overflow_display_title_once: Incomplete
    overflow_amalgamate_title: bool
    __tzinfo: Incomplete
    __store: Incomplete
    url_identifier: bool
    __cached_url_identifier: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize some general configuration that will keep things
        consistent when working with the notifiers that will inherit this
        class."""
    def image_url(self, notify_type: NotifyType, image_size: NotifyImageSize | None = None, logo: bool = False, extension: str | None = None) -> str | None:
        """Returns Image URL if possible."""
    def image_path(self, notify_type: NotifyType, extension: str | None = None) -> str | None:
        """Returns the path of the image if it can."""
    def image_raw(self, notify_type: NotifyType, extension: str | None = None) -> bytes | None:
        """Returns the raw image if it can."""
    def color(self, notify_type: NotifyType, color_type: type | None = None) -> str | int | tuple[int, int, int]:
        """Returns the html color (hex code) associated with the
        notify_type."""
    def ascii(self, notify_type: NotifyType) -> str:
        """Returns the ascii characters associated with the notify_type."""
    def notify(self, *args: Any, **kwargs: Any) -> bool:
        """Performs notification."""
    async def async_notify(self, *args: Any, **kwargs: Any) -> bool:
        """Performs notification for asynchronous callers."""
    def _build_send_calls(self, body: str | None = None, title: str | None = None, notify_type: NotifyType = ..., overflow: str | OverflowMode | None = None, attach: list[str] | AppriseAttachment | None = None, body_format: NotifyFormat | None = None, **kwargs: Any) -> Generator[dict[str, Any], None, None]:
        """Get a list of dictionaries that can be used to call send() or (in
        the future) async_send()."""
    def _apply_overflow(self, body: str | None, title: str | None = None, overflow: str | OverflowMode | None = None, body_format: NotifyFormat | None = None) -> list[dict[str, str]]:
        """
        Apply overflow behaviour (UPSTREAM, TRUNCATE, SPLIT) to title/body.

        Takes the message body and title as input.  This function then
        applies any defined overflow restrictions associated with the
        notification service and may alter the message if/as required.

        The function will always return a list object in the following
        structure:
            [
                {
                    title: 'the title goes here',
                    body: 'the message body goes here',
                },
                {
                    title: 'the title goes here',
                    body: 'the continued message body goes here',
                },
            ]
        """
    def send(self, body: str, title: str = '', notify_type: NotifyType = ..., **kwargs: Any) -> bool:
        """Should preform the actual notification itself."""
    def url_parameters(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        """Provides a default set of parameters to work with.

        This can greatly simplify URL construction in the acommpanied url()
        function in all defined plugin services.
        """
    @staticmethod
    def parse_url(url: str, verify_host: bool = True, plus_to_space: bool = False) -> dict[str, Any] | None:
        """Parses the URL and returns it broken apart into a dictionary.

        This is very specific and customized for Apprise.


        Args:
            url (str): The URL you want to fully parse.
            verify_host (:obj:`bool`, optional): a flag kept with the parsed
                 URL which some child classes will later use to verify SSL
                 keys (if SSL transactions take place).  Unless under very
                 specific circumstances, it is strongly recomended that
                 you leave this default value set to True.

        Returns:
            A dictionary is returned containing the URL fully parsed if
            successful, otherwise None is returned.
        """
    @staticmethod
    def parse_native_url(url: str) -> dict[str, Any] | None:
        """This is a base class that can be optionally over-ridden by child
        classes who can build their Apprise URL based on the one provided by
        the notification service they choose to use.

        The intent of this is to make Apprise a little more userfriendly to
        people who aren't familiar with constructing URLs and wish to use the
        ones that were just provied by their notification serivice that they're
        using.

        This function will return None if the passed in URL can't be matched as
        belonging to the notification service. Otherwise this function should
        return the same set of results that parse_url() does.
        """
    @property
    def store(self):
        """Returns a pointer to our persistent store for use.

        The best use cases are:
         self.store.get('key')
         self.store.set('key', 'value')
         self.store.delete('key1', 'key2', ...)

        You can also access the keys this way:
         self.store['key']

        And clear them:
         del self.store['key']
        """
    @property
    def tzinfo(self) -> tzinfo:
        """Returns our tzinfo file associated with this plugin if set
        otherwise the default timezone is returned.
        """
