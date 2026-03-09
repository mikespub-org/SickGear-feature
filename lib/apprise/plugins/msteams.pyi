from ..apprise_attachment import AppriseAttachment as AppriseAttachment
from ..common import NotifyFormat as NotifyFormat, NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from ..utils.parse import parse_bool as parse_bool, validate_regex as validate_regex
from ..utils.templates import TemplateType as TemplateType, apply_template as apply_template
from .base import NotifyBase as NotifyBase
from _typeshed import Incomplete

class NotifyMSTeams(NotifyBase):
    """A wrapper for Microsoft Teams Notifications."""
    service_name: str
    service_url: str
    secure_protocol: str
    setup_url: str
    notify_url_v1: str
    notify_url_v2: str
    notify_url_v3: str
    image_size: Incomplete
    body_maxlen: int
    notify_format: Incomplete
    max_msteams_template_size: int
    templates: Incomplete
    template_tokens: Incomplete
    template_args: Incomplete
    template_kwargs: Incomplete
    version: Incomplete
    team: Incomplete
    token_a: Incomplete
    token_b: Incomplete
    token_c: Incomplete
    token_d: Incomplete
    include_image: Incomplete
    template: Incomplete
    tokens: Incomplete
    def __init__(self, token_a, token_b, token_c, token_d=None, team=None, version=None, include_image: bool = True, template=None, tokens=None, **kwargs) -> None:
        """Initialize Microsoft Teams Object.

        You can optional specify a template and identify arguments you
        wish to populate your template with when posting.  Some reserved
        template arguments that can not be over-ridden are:
           `body`, `title`, and `type`.
        """
    def gen_payload(self, body, title: str = '', notify_type=..., **kwargs):
        """This function generates our payload whether it be the generic one
        Apprise generates by default, or one provided by a specified external
        template."""
    def send(self, body, title: str = '', notify_type=..., **kwargs):
        """Perform Microsoft Teams Notification."""
    @property
    def url_identifier(self):
        """Returns all of the identifiers that make this URL unique from
        another simliar one.

        Targets or end points should never be identified here.
        """
    def url(self, privacy: bool = False, *args, **kwargs):
        """Returns the URL built dynamically based on specified arguments."""
    @staticmethod
    def parse_url(url):
        """Parses the URL and returns enough arguments that can allow us to re-
        instantiate this object."""
    @staticmethod
    def parse_native_url(url):
        """
        Legacy Support:
            https://outlook.office.com/webhook/ABCD/IncomingWebhook/DEFG/HIJK

        New Hook Support:
            https://team-name.office.com/webhook/ABCD/IncomingWebhook/DEFG/HIJK

        Newer Hook Support:
            https://team-name.office.com/webhook/ABCD/IncomingWebhook/DEFG/HIJK/V2LMNOP
        """
