from ...asset import AppriseAsset as AppriseAsset
from ...common import NotifyType as NotifyType
from ...utils.parse import parse_bool as parse_bool
from _typeshed import Incomplete

class FCMColorManager:
    """A Simple object to accept either a boolean value.

    - True: Use colors provided by Apprise
    - False: Do not use colors at all
    - rrggbb: where you provide the rgb values (hence #333333)
    - rgb: is also accepted as rgb values (hence #333)

    For RGB colors, the hashtag is optional
    """
    __color_rgb: Incomplete
    asset: Incomplete
    color: Incomplete
    def __init__(self, color, asset=None) -> None:
        """Parses the color object accordingly."""
    def get(self, notify_type=...):
        """Returns color or true/false value based on configuration."""
    def __str__(self) -> str:
        """Our color representation."""
    def __bool__(self) -> bool:
        """Allows this object to be wrapped in an 'if statement'.

        True is returned if a color was loaded
        """
