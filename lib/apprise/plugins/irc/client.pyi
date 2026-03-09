from ...logger import logger as logger
from ...utils.socket import AppriseSocketError as AppriseSocketError, SocketTransport as SocketTransport
from .protocol import IRCAuthMode as IRCAuthMode, is_ping as is_ping, normalise_channel as normalise_channel, parse_irc_line as parse_irc_line, ping_payload as ping_payload
from .state import IRCActionKind as IRCActionKind, IRCContext as IRCContext, IRCStateMachine as IRCStateMachine
from _typeshed import Incomplete
from typing import Callable

NickGenerator = Callable[[str, int, int], str]

class IRCClient:
    """Socket-driven IRC Client."""
    default_insecure_port: int
    default_secure_port: int
    pump_interval: float
    nickname_max_length: int
    nickname_collision_max: int
    transport: Incomplete
    _nick_generator: Incomplete
    _nick_length: Incomplete
    _nick_collision: int
    auth_mode: Incomplete
    sm: Incomplete
    _out_queue: Deque[bytes]
    _inbuf: Incomplete
    def __init__(self, host: str, nickname: str, fullname: str, port: int | None = None, secure: bool = False, verify: bool = True, timeout: float | None = None, password: str | None = None, auth_mode: str = ..., nick_generator: NickGenerator | None = None, nick_length: int | None = None) -> None: ...
    @property
    def nickname(self) -> str:
        """Returns the accepted nickname."""
    def connect(self) -> None: ...
    def close(self) -> None: ...
    def _queue(self, line: str) -> None:
        """
        Queues message for outbound delivery to the IRC Server
        """
    def _write(self, line: str | bytes, deadline: float) -> None:
        """Write content directly to IRC."""
    def _flush(self, deadline: float) -> None:
        """Flush all queued information to the IRC server."""
    def _read(self, deadline: float) -> str | None:
        """
        Read incoming content from IRC Server
        """
    def _nickname_collision_handler(self, prefix: str) -> str: ...
    def _tick(self, deadline: float) -> float: ...
    def _handshake(self, deadline: float, prefix: str) -> None: ...
    def register(self, timeout: float, prefix: str) -> None:
        """Register with the IRC server, and optionally NickServ identify.

        - SERVER mode: sends PASS during registration (if password provided)
        - NICKSERV mode: does not send PASS, performs NickServ IDENTIFY after
          registration completes
        - NONE mode: no authentication is performed
        """
    def check_connection(self, timeout: float) -> bool:
        """Verify we can talk to the server by completing a PING/PONG."""
    def join(self, channel: str, timeout: float, prefix: str, key: str | None = None) -> None: ...
    def privmsg(self, target: str, message: str, timeout: float) -> None:
        """Handle the sending of private messages."""
    def identify(self, timeout: float) -> None:
        """Identify with NickServ after registration."""
    def quit(self, message: str, timeout: float) -> None: ...
    @staticmethod
    def nick_generation(prefix: str, length: int | None = None, collision: int = 0) -> str:
        """Generate a nickname suitable for retry after collision."""
