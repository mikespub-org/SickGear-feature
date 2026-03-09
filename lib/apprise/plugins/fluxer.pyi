from ..attachment.base import AttachBase as AttachBase
from ..common import NotifyFormat as NotifyFormat, NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from ..utils.parse import is_hostname as is_hostname, is_ipaddr as is_ipaddr, parse_bool as parse_bool, parse_list as parse_list, validate_regex as validate_regex
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete
from typing import Any

USER_ROLE_DETECTION_RE: Incomplete

class FluxerMode:
    """Define Fluxer Notification Modes."""
    CLOUD: str
    PRIVATE: str

FLUXER_MODES: Incomplete

class NotifyFluxer(NotifyBase):
    """A wrapper for Fluxer Webhook Notifications."""
    service_name: str
    service_url: str
    setup_url: str
    protocol: str
    secure_protocol: str
    image_size: Incomplete
    request_rate_per_sec: int
    attachment_support: bool
    fluxer_max_files: int
    default_delay_sec: float
    body_maxlen: int
    overflow_amalgamate_title: bool
    fluxer_max_fields: int
    __auto_cloud_host: Incomplete
    cloud_notify_host: str
    notify_url: str
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    webhook_id: Incomplete
    webhook_token: Incomplete
    mode: Incomplete
    tts: Incomplete
    avatar: Incomplete
    footer: Incomplete
    footer_logo: Incomplete
    include_image: Incomplete
    fields: Incomplete
    thread_id: Incomplete
    thread_name: Incomplete
    avatar_url: Incomplete
    href: Incomplete
    flags: Incomplete
    ping: list[str]
    ratelimit_reset: Incomplete
    ratelimit_remaining: Incomplete
    def __init__(self, webhook_id: str, webhook_token: str, mode: str | None = None, tts: bool = False, avatar: bool = True, footer: bool = False, footer_logo: bool = True, include_image: bool = False, fields: bool = True, avatar_url: str | None = None, href: str | None = None, thread: str | None = None, thread_name: str | None = None, flags: int | None = None, ping: list[str] | None = None, **kwargs: Any) -> None:
        """Initialize Fluxer Object."""
    def send(self, body: str, title: str = '', notify_type: NotifyType = ..., attach=None, **kwargs: Any) -> bool:
        """Perform Fluxer Notification."""
    def _send(self, payload: dict[str, Any], params: dict[str, str] | None = None, rate_limit: int = 1, attach: AttachBase | None = None, **kwargs: Any) -> bool:
        """Wrapper to the requests (post) object."""
    def url(self, privacy: bool = False, *args: Any, **kwargs: Any) -> str:
        """Returns the URL built dynamically based on specified arguments."""
    @property
    def url_identifier(self) -> tuple[Any, ...]:
        """Returns all of the identifiers that make this URL unique."""
    @staticmethod
    def parse_url(url: str) -> dict[str, Any] | None:
        """Parses the URL and returns arguments for instantiating this object.

        Syntax:
          fluxer://webhook_id/webhook_token
        """
    @staticmethod
    def parse_native_url(url: str) -> dict[str, Any] | None:
        """
        Supported:
          - https://api.fluxer.app/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN
          - https://api.fluxer.app/v1/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN
        """
    def ping_payload(self, *args: str) -> dict[str, Any]:
        """Build allow_mentions + mention content."""
    @staticmethod
    def extract_markdown_sections(markdown: str) -> tuple[str, list[dict[str, str]]]:
        """Extract headers and their corresponding sections into embed
        fields."""
