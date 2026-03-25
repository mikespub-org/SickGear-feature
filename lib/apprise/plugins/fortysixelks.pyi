from ..common import NotifyType as NotifyType
from ..url import PrivacyMode as PrivacyMode
from ..utils.parse import is_phone_no as is_phone_no, parse_phone_no as parse_phone_no
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any

class Notify46Elks(NotifyBase):
    """A wrapper for 46elks Notifications."""
    service_name: Incomplete
    service_url: str
    secure_protocol: Incomplete
    setup_url: str
    notify_url: str
    title_maxlen: int
    body_maxlen: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    source: str | None
    targets: Incomplete
    def __init__(self, targets: Iterable[str] | None = None, source: str | None = None, **kwargs: Any) -> None:
        """
        Initialise 46elks notifier.

        :param targets: Iterable of phone numbers. E.164 is recommended.
        :param source: Optional source ID or E.164 number.
        """
    def send(self, body: str, title: str = '', notify_type: NotifyType = ..., **kwargs: Any) -> bool:
        """Perform 46elks Notification."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another similar one.

        Targets or end points should never be identified here.
        """
    def url(self, privacy: bool = False, *args: Any, **kwargs: Any) -> str:
        """Returns the URL built dynamically based on specified arguments."""
    def __len__(self) -> int:
        """Returns the number of targets associated with this notification."""
    @staticmethod
    def parse_native_url(url):
        """
        Support https://user:pw@api.46elks.com/a1/sms?to=+15551234567&from=Acme
        """
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
