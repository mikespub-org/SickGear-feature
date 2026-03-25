from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any

class NotifyViber(NotifyBase):
    """Send a Viber Bot message using the Viber REST Bot API."""
    service_name: Incomplete
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url: str
    body_maxlen: int
    title_maxlen: int
    viber_sender_name_limit: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    token: Incomplete
    source: str
    avatar: str | None
    targets: Incomplete
    def __init__(self, token: str, targets: Iterable[str] | None = None, source: str | None = None, avatar: str | None = None, **kwargs: Any) -> None: ...
    def __len__(self) -> int:
        """Number of outbound HTTP requests this configuration will perform."""
    def url(self, privacy: bool = False, *args: Any, **kwargs: Any) -> str:
        """Rebuild the Apprise URL with secrets redacted."""
    @property
    def url_identifier(self) -> str:
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def send(self, body: str, title: str = '', notify_type: NotifyType = ..., **kwargs: Any) -> bool:
        """Send a Viber notification to each configured receiver ID."""
    @staticmethod
    def parse_url(url: str) -> dict[str, Any]:
        """Parse the URL and return arguments to instantiate this object."""
