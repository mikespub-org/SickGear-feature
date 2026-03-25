from ..common import NOTIFY_IMAGE_SIZES as NOTIFY_IMAGE_SIZES, NOTIFY_TYPES as NOTIFY_TYPES, NotifyImageSize as NotifyImageSize, NotifyType as NotifyType
from .base import NotifyBase as NotifyBase

__all__ = ['NOTIFY_IMAGE_SIZES', 'NOTIFY_TYPES', 'NotifyBase', 'NotifyImageSize', 'NotifyType', 'url_to_dict']

def url_to_dict(url, secure_logging: bool = True):
    """Takes an apprise URL and returns the tokens associated with it if they
    can be acquired based on the plugins available.

    None is returned if the URL could not be parsed, otherwise the tokens are
    returned.

    These tokens can be loaded into apprise through it's add() function.
    """
