from . import emby as emby

class NotifyJellyfin(emby.NotifyEmby):
    """Send notifications to Jellyfin (Emby-compatible) servers."""
    service_name: str
    service_url: str
    protocol: str
    secure_protocol: str
    setup_url: str
