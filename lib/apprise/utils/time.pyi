from ..logger import logger as logger
from zoneinfo import ZoneInfo

def zoneinfo(name: str) -> ZoneInfo | None:
    """
    More forgiving ZoneInfo instantiation
    - Accepts lower/upper case
    - Normalises common UTC variants
    """
