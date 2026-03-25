from _typeshed import Incomplete

class IRCAuthMode:
    """IRC authentication mode.

    The IRC plugin uses a small set of authentication strategies, selected
    by URL parsing logic. These values are treated as constants and are used
    by the client (connection setup) rather than by the parsing/state code.

    NONE
        No authentication.
    SERVER
        Use PASS <password> during registration.
    NICKSERV
        Authenticate after registration via NickServ IDENTIFY.
    ZNC
        Connect to a ZNC bouncer and presume registration is already handled.
        In this mode, the client generally avoids emitting registration flows.
    """
    NONE: str
    SERVER: str
    NICKSERV: str
    ZNC: str

IRC_AUTH_MODES: Incomplete

class IRCMessage:
    """A parsed IRC line.

    raw
        The line as received (minus CRLF).
    prefix
        Optional prefix (nick/server). Examples:
            server.example
            nick!user@host
    command
        The IRC command, for example: PRIVMSG, JOIN, PING, or a numeric string.
    params
        A tuple of middle parameters (space separated).
    trailing
        The trailing parameter (after ' :'), which may contain spaces.

    Notes on numerics:
        Numeric replies are three digits as a string. This helper provides
        a .numeric property that returns an int, or None when not numeric.
    """
    raw: str
    prefix: str | None
    command: str
    params: tuple[str, ...]
    trailing: str | None
    @property
    def numeric(self) -> int | None:
        """Return numeric reply code as int when command is a 3-digit
        string."""

def parse_irc_line(line: str) -> IRCMessage:
    """Parse an IRC line into its components.

    This is intentionally tolerant and small, but sufficient for:
    - detecting PINGs (command == 'PING')
    - reading common numeric replies (001, 376/422, 366, error codes)
    - identifying JOIN completion
    - extracting the welcome nick from 001

    The parser follows the usual IRC split rules:
    - prefix is optional and begins with ':' at the start of the line
    - trailing is optional and begins with ' :' and consumes the remainder
    - params are any remaining space-delimited tokens after command
    """
def is_ping(msg: IRCMessage) -> bool:
    """True when message is a PING request."""
def ping_payload(msg: IRCMessage) -> str:
    """Extract the payload to use when responding to a PING."""
def extract_welcome_nick(msg: IRCMessage) -> str | None:
    """Extract the nickname from the numeric 001 (welcome) message."""
def normalise_channel(name: str) -> str:
    """Normalise a channel name to include '#'."""
