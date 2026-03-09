from ..common import ContentLocation as ContentLocation
from ..utils.disk import path_decode as path_decode
from .base import AttachBase as AttachBase
from _typeshed import Incomplete

class AttachFile(AttachBase):
    """A wrapper for File based attachment sources."""
    service_name: Incomplete
    protocol: str
    location: Incomplete
    dirty_path: Incomplete
    __original_path: Incomplete
    def __init__(self, path, **kwargs) -> None:
        """Initialize Local File Attachment Object."""
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    download_path: Incomplete
    detected_name: Incomplete
    def download(self, **kwargs):
        """Perform retrieval of our data.

        For file base attachments, our data already exists, so we only need to
        validate it.
        """
    @staticmethod
    def parse_url(url):
        """Parses the URL so that we can handle all different file paths and
        return it as our path object."""
