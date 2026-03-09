from _typeshed import Incomplete

class AppriseException(Exception):
    """Base Apprise Exception Class."""
    error_code: Incomplete
    def __init__(self, message, error_code: int = 0) -> None: ...

class ApprisePluginException(AppriseException):
    """Class object for handling exceptions raised from within a plugin."""
    def __init__(self, message, error_code: int = 600) -> None: ...

class AppriseDiskIOError(AppriseException):
    """Thrown when an disk i/o error occurs."""
    def __init__(self, message, error_code=...) -> None: ...

class AppriseInvalidData(AppriseException):
    """Thrown when bad data was passed into an internal function."""
    def __init__(self, message, error_code=...) -> None: ...

class AppriseFileNotFound(AppriseDiskIOError, FileNotFoundError):
    """Thrown when a persistent write occured in MEMORY mode."""
    def __init__(self, message) -> None: ...
