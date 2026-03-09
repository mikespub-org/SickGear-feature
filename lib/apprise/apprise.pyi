from . import __version__ as __version__, common as common, plugins as plugins
from .apprise_attachment import AppriseAttachment as AppriseAttachment
from .apprise_config import AppriseConfig as AppriseConfig
from .asset import AppriseAsset as AppriseAsset
from .common import ContentLocation as ContentLocation
from .config.base import ConfigBase as ConfigBase
from .conversion import convert_between as convert_between
from .emojis import apply_emojis as apply_emojis
from .locale import AppriseLocale as AppriseLocale
from .logger import logger as logger
from .manager_plugins import NotificationManager as NotificationManager
from .plugins.base import NotifyBase as NotifyBase
from .utils.cwe312 import cwe312_url as cwe312_url
from .utils.logic import is_exclusive_match as is_exclusive_match
from .utils.parse import parse_list as parse_list, parse_urls as parse_urls
from _typeshed import Incomplete
from collections.abc import Generator, Iterator
from typing import Any

N_MGR: Incomplete

class Apprise:
    """Our Notification Manager."""
    servers: Incomplete
    asset: Incomplete
    locale: Incomplete
    debug: Incomplete
    location: Incomplete
    def __init__(self, servers: str | dict | NotifyBase | AppriseConfig | ConfigBase | list[str | dict | NotifyBase | AppriseConfig | ConfigBase] | None = None, asset: AppriseAsset | None = None, location: ContentLocation | None = None, debug: bool = False) -> None:
        """Loads a set of server urls while applying the Asset() module to each
        if specified.

        If no asset is provided, then the default asset is used.

        Optionally specify a global ContentLocation for a more strict means of
        handling Attachments.
        """
    @staticmethod
    def instantiate(url: str | dict, asset: AppriseAsset | None = None, tag: str | list[str] | None = None, suppress_exceptions: bool = True) -> NotifyBase | None:
        """Returns the instance of a instantiated plugin based on the provided
        Server URL.  If the url fails to be parsed, then None is returned.

        The specified url can be either a string (the URL itself) or a
        dictionary containing all of the components needed to istantiate
        the notification service.  If identifying a dictionary, at the bare
        minimum, one must specify the schema.

        An example of a url dictionary object might look like:
          {
            schema: 'mailto',
            host: 'google.com',
            user: 'myuser',
            password: 'mypassword',
          }

        Alternatively the string is much easier to specify:
          mailto://user:mypassword@google.com

        The dictionary works well for people who are calling details() to
        extract the components they need to build the URL manually.
        """
    def add(self, servers: str | dict | NotifyBase | AppriseConfig | ConfigBase | list[str | dict | NotifyBase | AppriseConfig | ConfigBase], asset: AppriseAsset | None = None, tag: str | list[str] | None = None) -> bool:
        """Adds one or more server URLs into our list.

        You can override the global asset if you wish by including it with the
        server(s) that you add.

        The tag allows you to associate 1 or more tag values to the server(s)
        being added. tagging a service allows you to exclusively access them
        when calling the notify() function.
        """
    def clear(self) -> None:
        """Empties our server list."""
    def find(self, tag: Any = ..., match_always: bool = True) -> Iterator[NotifyBase]:
        """Returns a list of all servers matching against the tag specified."""
    def notify(self, body: str | bytes, title: str | bytes = '', notify_type: str | common.NotifyType = ..., body_format: str | None = None, tag: Any = ..., match_always: bool = True, attach: Any = None, interpret_escapes: bool | None = None) -> bool | None:
        """Send a notification to all the plugins previously loaded.

        If the body_format specified is NotifyFormat.MARKDOWN, it will be
        converted to HTML if the Notification type expects this.

        if the tag is specified (either a string or a set/list/tuple of
        strings), then only the notifications flagged with that tagged value
        are notified.  By default, all added services are notified
        (tag=MATCH_ALL_TAG)

        This function returns True if all notifications were successfully sent,
        False if even just one of them fails, and None if no notifications were
        sent at all as a result of tag filtering and/or simply having empty
        configuration files that were read.

        Attach can contain a list of attachment URLs.  attach can also be
        represented by an AttachBase() (or list of) object(s). This identifies
        the products you wish to notify

        Set interpret_escapes to True if you want to pre-escape a string such
        as turning a 
 into an actual new line, etc.
        """
    async def async_notify(self, *args: Any, **kwargs: Any) -> bool | None:
        """Send a notification to all the plugins previously loaded, for
        asynchronous callers.

        The arguments are identical to those of Apprise.notify().
        """
    def _create_notify_calls(self, *args, **kwargs):
        """Creates notifications for all the plugins loaded.

        Returns a list of (server, notify() kwargs) tuples for plugins with
        parallelism disabled and another list for plugins with parallelism
        enabled.
        """
    def _create_notify_gen(self, body, title: str = '', notify_type=..., body_format=None, tag=..., match_always: bool = True, attach=None, interpret_escapes=None) -> Generator[Incomplete]:
        """Internal generator function for _create_notify_calls()."""
    @staticmethod
    def _notify_sequential(*servers_kwargs):
        """Process a list of notify() calls sequentially and synchronously."""
    @staticmethod
    def _notify_parallel_threadpool(*servers_kwargs):
        """Process a list of notify() calls in parallel and synchronously."""
    @staticmethod
    async def _notify_parallel_asyncio(*servers_kwargs):
        """Process a list of async_notify() calls in parallel and
        asynchronously."""
    def details(self, lang: str | None = None, show_requirements: bool = False, show_disabled: bool = False) -> dict[str, Any]:
        """Returns the details associated with the Apprise object."""
    def urls(self, privacy: bool = False) -> list[str]:
        """Returns all of the loaded URLs defined in this apprise object."""
    def pop(self, index: int) -> NotifyBase:
        """Removes an indexed Notification Service from the stack and returns
        it.

        The thing is we can never pop AppriseConfig() entries, only what was
        loaded within them. So pop needs to carefully iterate over our list and
        only track actual entries.
        """
    def __getitem__(self, index: int) -> NotifyBase:
        """Returns the indexed server entry of a loaded notification server."""
    def __getstate__(self) -> dict[str, object]:
        """Pickle Support dumps()"""
    def __setstate__(self, state: dict[str, object]) -> None:
        """Pickle Support loads()"""
    def __bool__(self) -> bool:
        """Allows the Apprise object to be wrapped in an 'if statement'.

        True is returned if at least one service has been loaded.
        """
    def __iter__(self) -> Iterator[NotifyBase]:
        """Returns an iterator to each of our servers loaded.

        This includes those found inside configuration.
        """
    def __len__(self) -> int:
        """Returns the number of servers loaded; this includes those found
        within loaded configuration.

        This funtion nnever actually counts the Config entry themselves (if
        they exist), only what they contain.
        """
