from .asset import AppriseAsset as AppriseAsset
from .attachment.base import AttachBase as AttachBase
from .common import ContentLocation as ContentLocation
from .logger import logger as logger
from .manager_attachment import AttachmentManager as AttachmentManager
from .url import URLBase as URLBase
from .utils.parse import GET_SCHEMA_RE as GET_SCHEMA_RE
from _typeshed import Incomplete
from collections.abc import Iterator
from typing import Any

A_MGR: Incomplete

class AppriseAttachment:
    """Our Apprise Attachment File Manager."""
    attachments: Incomplete
    cache: Incomplete
    asset: Incomplete
    location: Incomplete
    def __init__(self, paths: str | list[str | AttachBase | AppriseAttachment] | None = None, asset: AppriseAsset | None = None, cache: bool | int = True, location: str | ContentLocation | None = None, **kwargs: Any) -> None:
        """Loads all of the paths/urls specified (if any).

        The path can either be a single string identifying one explicit
        location, otherwise you can pass in a series of locations to scan
        via a list.

        By default we cache our responses so that subsiquent calls does not
        cause the content to be retrieved again.  For local file references
        this makes no difference at all.  But for remote content, this does
        mean more then one call can be made to retrieve the (same) data.  This
        method can be somewhat inefficient if disabled.  Only disable caching
        if you understand the consequences.

        You can alternatively set the cache value to an int identifying the
        number of seconds the previously retrieved can exist for before it
        should be considered expired.

        It's also worth nothing that the cache value is only set to elements
        that are not already of subclass AttachBase()

        Optionally set your current ContentLocation in the location argument.
        This is used to further handle attachments. The rules are as follows:
          - INACCESSIBLE: You simply have disabled use of the object; no
                          attachments will be retrieved/handled.
          - HOSTED:       You are hosting an attachment service for others.
                          In these circumstances all attachments that are LOCAL
                          based (such as file://) will not be allowed.
          - LOCAL:        The least restrictive mode as local files can be
                          referenced in addition to hosted.

        In all but HOSTED and LOCAL modes, INACCESSIBLE attachment types will
        continue to be inaccessible.  However if you set this field (location)
        to None (it's default value) the attachment location category will not
        be tested in any way (all attachment types will be allowed).

        The location field is also a global option that can be set when
        initializing the Apprise object.
        """
    def add(self, attachments: str | AttachBase | AppriseAttachment | list[str | AttachBase | AppriseAttachment], asset: AppriseAsset | None = None, cache: bool | int | None = None) -> bool:
        """Adds one or more attachments into our list.

        By default we cache our responses so that subsiquent calls does not
        cause the content to be retrieved again.  For local file references
        this makes no difference at all.  But for remote content, this does
        mean more then one call can be made to retrieve the (same) data.  This
        method can be somewhat inefficient if disabled.  Only disable caching
        if you understand the consequences.

        You can alternatively set the cache value to an int identifying the
        number of seconds the previously retrieved can exist for before it
        should be considered expired.

        It's also worth nothing that the cache value is only set to elements
        that are not already of subclass AttachBase()
        """
    @staticmethod
    def instantiate(url: str, asset: AppriseAsset | None = None, cache: bool | int | None = None, suppress_exceptions: bool = True) -> AttachBase | None:
        """Returns the instance of a instantiated attachment plugin based on
        the provided Attachment URL.  If the url fails to be parsed, then None
        is returned.

        A specified cache value will over-ride anything set
        """
    def sync(self, abort_on_error: bool = True, abort_if_empty: bool = True) -> bool:
        """Itereates over all of the attachments and retrieves them."""
    def clear(self) -> None:
        """Empties our attachment list."""
    def size(self) -> int:
        """Returns the total size of accumulated attachments."""
    def pop(self, index: int = -1) -> AttachBase:
        """Removes an indexed Apprise Attachment from the stack and returns it.

        by default the last element is poped from the list
        """
    def __getitem__(self, index: int) -> AttachBase:
        """Returns the indexed entry of a loaded apprise attachments."""
    def __bool__(self) -> bool:
        """Allows the Apprise object to be wrapped in an 'if statement'.

        True is returned if at least one service has been loaded.
        """
    def __iter__(self) -> Iterator[AttachBase]:
        """Returns an iterator to our attachment list."""
    def __len__(self) -> int:
        """Returns the number of attachment entries loaded."""
