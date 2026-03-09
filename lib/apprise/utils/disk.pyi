from ..logger import logger as logger
from _typeshed import Incomplete

ESCAPED_PATH_SEPARATOR: Incomplete
ESCAPED_WIN_PATH_SEPARATOR: Incomplete
ESCAPED_NUX_PATH_SEPARATOR: Incomplete
TIDY_WIN_PATH_RE: Incomplete
TIDY_WIN_TRIM_RE: Incomplete
TIDY_NUX_PATH_RE: Incomplete
__PATH_DECODER: Incomplete

def path_decode(path):
    """Returns the fully decoded path based on the operating system."""
def tidy_path(path):
    """Take a filename and or directory and attempts to tidy it up by removing
    trailing slashes and correcting any formatting issues.

    For example: ////absolute//path// becomes:
        /absolute/path
    """
def dir_size(path, max_depth: int = 3, missing_okay: bool = True, _depth: int = 0, _errors=None):
    """Scans a provided path an returns it's size (in bytes) of path
    provided."""
def bytes_to_str(value):
    """Covert an integer (in bytes) into it's string representation with
    acompanied unit value (such as B, KB, MB, GB, TB, etc)"""
