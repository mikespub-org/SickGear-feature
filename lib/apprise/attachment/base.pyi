import types
from .. import exception as exception
from ..common import ContentLocation as ContentLocation
from ..url import URLBase as URLBase
from ..utils.parse import parse_bool as parse_bool
from _typeshed import Incomplete
from collections.abc import Generator

class AttachBase(URLBase):
    """This is the base class for all supported attachment types."""
    max_detect_buffer_size: int
    unknown_mimetype: str
    unknown_filename: str
    unknown_filename_extension: str
    strict: bool
    max_file_size: int
    location: Incomplete
    template_args: Incomplete
    _name: Incomplete
    _mimetype: Incomplete
    detected_mimetype: Incomplete
    detected_name: Incomplete
    download_path: Incomplete
    __pointers: Incomplete
    cache: Incomplete
    def __init__(self, name=None, mimetype=None, cache=None, **kwargs) -> None:
        """Initialize some general logging and common server arguments that
        will keep things consistent when working with the configurations that
        inherit this class.

        Optionally provide a filename to over-ride name associated with the
        actual file retrieved (from where-ever).

        The mime-type is automatically detected, but you can over-ride this by
        explicitly stating what it should be.

        By default we cache our responses so that subsiquent calls does not
        cause the content to be retrieved again.  For local file references
        this makes no difference at all.  But for remote content, this does
        mean more then one call can be made to retrieve the (same) data.  This
        method can be somewhat inefficient if disabled.  Only disable caching
        if you understand the consequences.

        You can alternatively set the cache value to an int identifying the
        number of seconds the previously retrieved can exist for before it
        should be considered expired.
        """
    @property
    def path(self):
        """Returns the absolute path to the filename.

        If this is not known or is know but has been considered expired (due to
        cache setting), then content is re-retrieved prior to returning.
        """
    @property
    def name(self):
        """Returns the filename."""
    @property
    def mimetype(self):
        """Returns mime type (if one is present).

        Content is cached once determied to prevent overhead of future calls.
        """
    def exists(self, retrieve_if_missing: bool = True):
        """Simply returns true if the object has downloaded and stored the
        attachment AND the attachment has not expired."""
    def base64(self, encoding: str = 'ascii'):
        """Returns the attachment object as a base64 string otherwise None is
        returned if an error occurs.

        If encoding is set to None, then it is not encoded when returned
        """
    def invalidate(self) -> None:
        """Release any temporary data that may be open by child classes.
        Externally fetched content should be automatically cleaned up when this
        function is called.

        This function should also reset the following entries to None:
          - detected_name : Should identify a human readable filename
          - download_path: Must contain a absolute path to content
          - detected_mimetype: Should identify mimetype of content
        """
    def download(self) -> None:
        """This function must be over-ridden by inheriting classes.

        Inherited classes MUST populate:
          - detected_name: Should identify a human readable filename
          - download_path: Must contain a absolute path to content
          - detected_mimetype: Should identify mimetype of content

        If a download fails, you should ensure these values are set to None.
        """
    def open(self, mode: str = 'rb'):
        """Return our file pointer and track it (we'll auto close later)"""
    def chunk(self, size: int = 5242880) -> Generator[Incomplete]:
        """A Generator that yield chunks of a file with the specified size.

        By default the chunk size is set to 5MB (5242880 bytes)
        """
    def __enter__(self):
        """Support with keyword."""
    def __exit__(self, value_type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None:
        """Stub to do nothing; but support exit of with statement
        gracefully."""
    @staticmethod
    def parse_url(url, verify_host: bool = True, mimetype_db=None, sanitize: bool = True):
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
    def __len__(self) -> int:
        """Returns the filesize of the attachment."""
    def __bool__(self) -> bool:
        """Allows the Apprise object to be wrapped in an based 'if statement'.

        True is returned if our content was downloaded correctly.
        """
    def __del__(self) -> None:
        """Perform any house cleaning."""
