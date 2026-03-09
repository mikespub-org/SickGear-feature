import types
from _typeshed import Incomplete

LOGGER_NAME: str

def trace(self, message, *args, **kwargs) -> None:
    """
    Verbose Debug Logging - Trace
    """
def deprecate(self, message, *args, **kwargs) -> None:
    """Deprication Warning Logging."""

logger: Incomplete

class LogCapture:
    '''A class used to allow one to instantiate loggers that write to memory
    for temporary purposes. e.g.:

    1.  with LogCapture() as captured:
    2.
    3.      # Send our notification(s)
    4.      aobj.notify("hello world")
    5.
    6.      # retrieve our logs produced by the above call via our
    7.      # `captured` StringIO object we have access to within the `with`
    8.      # block here:
    9.      print(captured.getvalue())
    '''
    __buffer_ptr: Incomplete
    __path: Incomplete
    __delete: Incomplete
    __level: Incomplete
    __restore_level: Incomplete
    __logger: Incomplete
    __handler: Incomplete
    def __init__(self, path=None, level=None, name=..., delete: bool = True, fmt: str = '%(asctime)s - %(levelname)s - %(message)s') -> None:
        """Instantiate a temporary log capture object.

        If a path is specified, then log content is sent to that file instead
        of a StringIO object.

        You can optionally specify a logging level such as logging.INFO if you
        wish, otherwise by default the script uses whatever logging has been
        set globally. If you set delete to `False` then when using log files,
        they are not automatically cleaned up afterwards.

        Optionally over-ride the fmt as well if you wish.
        """
    def __enter__(self):
        """Allows logger manipulation within a 'with' block."""
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: types.TracebackType | None):
        """Removes the handler gracefully when the with block has completed."""
