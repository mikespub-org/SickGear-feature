import socket
import ssl
from ..exception import AppriseException as AppriseException, AppriseInvalidData as AppriseInvalidData
from ..logger import logger as logger
from _typeshed import Incomplete

TimeoutType = float | tuple[float | None, float | None] | None

class AppriseSocketError(AppriseException):
    """Raised for socket or TLS related failures."""

class SocketTransport:
    """
    TCP client transport with optional TLS upgrade.

    Behaviour:
      - secure=False (default): plain TCP
      - secure=True: upgrade to TLS (immediately in connect(), or manually via
        start_tls())
      - verify=True (default): validate certificate chain and hostname using a
        certifi CA bundle
      - verify=False: accept invalid or self-signed certs

    Timeout behaviour (requests-compatible):
      - timeout=float => (connect, read) both set to float
      - timeout=(connect, read) => tuple form
      - None => no defaults (connect/read can block indefinitely)
    """
    host: Incomplete
    port: Incomplete
    bind_addr: Incomplete
    bind_port: Incomplete
    secure: Incomplete
    verify: Incomplete
    retries: Incomplete
    _sock: socket.socket | None
    _rfile: Incomplete
    _wfile: Incomplete
    _is_tls: bool
    _had_io: bool
    local_addr: tuple[str, int] | None
    remote_addr: tuple[str, int] | None
    def __init__(self, host: str, port: int, bind_addr: str | None = None, bind_port: int | None = None, secure: bool = False, verify: bool = True, timeout: TimeoutType = 10.0, retries: int = 0) -> None: ...
    @staticmethod
    def _coerce_timeout(timeout: TimeoutType) -> tuple[float | None, float | None]:
        """
        Coerce requests-style timeout into (connect_timeout, read_timeout).
        """
    @property
    def connected(self) -> bool: ...
    @property
    def is_tls(self) -> bool: ...
    def close(self) -> None:
        """Close the socket and associated file wrappers."""
    def _refresh_wrappers(self) -> None:
        """Rebuild file wrappers, required after TLS upgrade."""
    def can_read(self, timeout: float = 0.0) -> bool | None:
        """Return True if readable, False if not, None if closed or error."""
    def can_write(self, timeout: float = 0.0) -> bool | None:
        """Return True if writable, False if not, None if closed or error."""
    def connect(self) -> None:
        """
        Establish TCP connection, optionally upgrade to TLS immediately if
        secure=True.
        """
    def _server_hostname_for_tls(self) -> str:
        """
        Determine hostname used for SNI and hostname verification.

        If verify=True and host is an IP address, attempt reverse DNS lookup.
        """
    def _build_ssl_context(self) -> ssl.SSLContext:
        """Build SSL context using certifi bundle when verify=True."""
    def start_tls(self) -> None:
        """Upgrade an existing TCP connection to TLS."""
    def _attempt_reconnect(self, retries: int, action: str, exc: Exception) -> bool:
        '''
        Attempt to reconnect and allow the caller to retry.

        Args:
            retries: Remaining reconnect attempts permitted (<= 0 disables).
            action: A short label (e.g. "read" or "write") for logging.
            exc: The exception that triggered the reconnect attempt.

        Returns:
            True if a reconnect was performed and the caller should retry.
        '''
    def read(self, max_bytes: int = 32768, blocking: bool = False, timeout: float | None = None, retries: int | None = None) -> bytes:
        '''
        Read up to max_bytes bytes.

        blocking=False:
          - returns immediately with available data, or b"" if none

        blocking=True:
          - waits up to timeout seconds (or instance read timeout if timeout is
            None), then reads once
          - if both are None, waits indefinitely

        retries:
          - number of reconnect attempts permitted if the socket goes stale
            after prior successful I/O. Defaults to None (which takes value
            globally passed into the class)
        '''
    def write(self, data: bytes, flush: bool = True, timeout: float | None = None, retries: int | None = None) -> int:
        """
        Write bytes to the socket.

        timeout:
          - if None, uses instance read timeout
          - if both are None, blocks until complete

        retries:
          - number of reconnect attempts permitted if the socket goes stale
            after prior successful I/O. Defaults to None (which takes value
            globally passed into the class)
        """
