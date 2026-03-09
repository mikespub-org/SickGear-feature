from . import templates as templates
from ...common import NotifyType as NotifyType
from ...url import PrivacyMode as PrivacyMode
from ...utils.parse import parse_bool as parse_bool, parse_list as parse_list
from ...utils.socket import AppriseSocketError as AppriseSocketError
from ..base import NotifyBase as NotifyBase
from .client import IRCClient as IRCClient
from .protocol import IRCAuthMode as IRCAuthMode, IRC_AUTH_MODES as IRC_AUTH_MODES, normalise_channel as normalise_channel
from _typeshed import Incomplete
from typing import Any

IS_USER: Incomplete
IS_CHANNEL: Incomplete

class NotifyIRC(NotifyBase):
    """A wrapper to IRC servers using TCP or TLS."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    setup_url: str
    body_maxlen: int
    irc_register_timeout: float
    request_rate_per_sec: float
    title_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    join: Incomplete
    nickname: Incomplete
    auth_mode: Incomplete
    fullname: Incomplete
    channels: dict[str, str | None]
    users: list[str]
    join_timeout: Incomplete
    send_timeout: Incomplete
    targets: Incomplete
    def __init__(self, targets: list[str] | None = None, name: str | None = None, join: bool | None = None, nick: str | None = None, mode: str | None = None, **kwargs: Any) -> None: ...
    secure: Incomplete
    port: Incomplete
    def apply_irc_defaults(self, port=None, **kwargs) -> None:
        """
        A function that prefills defaults based on the irc details
        provided.
        """
    def send(self, body: str, title: str = '', notify_type: NotifyType = ..., attach: Any = None, **kwargs: Any) -> bool:
        """Send a notification to IRC targets."""
    @property
    def url_identifier(self) -> tuple[str, str | None, str | None, str | None]:
        """Return the pieces that uniquely identify this configuration."""
    def url(self, privacy: bool = False, *args: Any, **kwargs: Any) -> str:
        """Return the URL representation of this notification."""
    @staticmethod
    def parse_url(url: str) -> dict[str, Any] | None:
        """Parse an IRC URL into constructor arguments."""
