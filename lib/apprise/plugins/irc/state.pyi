from .protocol import IRCMessage as IRCMessage, extract_welcome_nick as extract_welcome_nick
from _typeshed import Incomplete
from enum import Enum

class IRCState(Enum):
    """High-level connection state."""
    DISCONNECTED = ...
    REGISTERING = ...
    READY = ...
    JOINING = ...
    QUITTING = ...
    ERROR = ...

class IRCActionKind(Enum):
    """Action returned by the state machine."""
    SEND = ...
    FAIL = ...
    NOOP = ...

class IRCAction:
    """Represents the next step for the client."""
    kind: IRCActionKind
    line: str | None
    reason: str | None

class IRCContext:
    """Mutable context shared between client and state machine."""
    desired_nick: str
    accepted_nick: str
    fullname: str
    password: str | None
    registered: bool
    motd_done: bool
    joined: set[str]
    last_error: str | None

def _err(msg: IRCMessage) -> str:
    """Build a human readable error message from an IRC message."""

REGISTER_ERRORS: Incomplete
JOIN_ERRORS: Incomplete

class IRCStateMachine:
    """State machine driven by inbound IRC messages."""
    ctx: Incomplete
    state: IRCState
    def __init__(self, ctx: IRCContext) -> None: ...
    def start_registration(self) -> list[IRCAction]:
        """Begin registration by emitting PASS/NICK/USER as required."""
    def on_message(self, msg: IRCMessage) -> list[IRCAction]:
        """Process an inbound IRC message and emit next actions."""
    def request_join(self, channel: str, key: str | None = None) -> list[IRCAction]:
        """Request a channel join and enter JOINING state."""
    def request_quit(self, message: str) -> list[IRCAction]:
        """Request a quit and enter QUITTING state."""
