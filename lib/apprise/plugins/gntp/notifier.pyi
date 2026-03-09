from _typeshed import Incomplete

__all__ = ['mini', 'GrowlNotifier']

class GrowlNotifier:
    """Helper class to simplfy sending Growl messages

\t:param string applicationName: Sending application name
\t:param list notification: List of valid notifications
\t:param list defaultNotifications: List of notifications that should be enabled
\t\tby default
\t:param string applicationIcon: Icon URL
\t:param string hostname: Remote host
\t:param integer port: Remote port
\t"""
    passwordHash: str
    socketTimeout: int
    applicationName: Incomplete
    notifications: Incomplete
    defaultNotifications: Incomplete
    applicationIcon: Incomplete
    password: Incomplete
    hostname: Incomplete
    port: Incomplete
    def __init__(self, applicationName: str = 'Python GNTP', notifications=[], defaultNotifications=None, applicationIcon=None, hostname: str = 'localhost', password=None, port: int = 23053) -> None: ...
    def _checkIcon(self, data):
        """
\t\tCheck the icon to see if it's valid

\t\tIf it's a simple URL icon, then we return True. If it's a data icon
\t\tthen we return False
\t\t"""
    def register(self):
        """Send GNTP Registration

\t\t.. warning::
\t\t\tBefore sending notifications to Growl, you need to have
\t\t\tsent a registration message at least once
\t\t"""
    def notify(self, noteType, title, description, icon=None, sticky: bool = False, priority=None, callback=None, identifier=None, custom={}):
        """Send a GNTP notifications

\t\t.. warning::
\t\t\tMust have registered with growl beforehand or messages will be ignored

\t\t:param string noteType: One of the notification names registered earlier
\t\t:param string title: Notification title (usually displayed on the notification)
\t\t:param string description: The main content of the notification
\t\t:param string icon: Icon URL path
\t\t:param boolean sticky: Sticky notification
\t\t:param integer priority: Message priority level from -2 to 2
\t\t:param string callback:  URL callback
\t\t:param dict custom: Custom attributes. Key names should be prefixed with X-
\t\t\taccording to the spec but this is not enforced by this class

\t\t.. warning::
\t\t\tFor now, only URL callbacks are supported. In the future, the
\t\t\tcallback argument will also support a function
\t\t"""
    def subscribe(self, id, name, port):
        """Send a Subscribe request to a remote machine"""
    def add_origin_info(self, packet) -> None:
        """Add optional Origin headers to message"""
    def register_hook(self, packet) -> None: ...
    def notify_hook(self, packet) -> None: ...
    def subscribe_hook(self, packet) -> None: ...
    def _send(self, messagetype, packet):
        """Send the GNTP Packet"""

def mini(description, applicationName: str = 'PythonMini', noteType: str = 'Message', title: str = 'Mini Message', applicationIcon=None, hostname: str = 'localhost', password=None, port: int = 23053, sticky: bool = False, priority=None, callback=None, notificationIcon=None, identifier=None, notifierFactory=...):
    """Single notification function

\tSimple notification function in one line. Has only one required parameter
\tand attempts to use reasonable defaults for everything else
\t:param string description: Notification message

\t.. warning::
\t\t\tFor now, only URL callbacks are supported. In the future, the
\t\t\tcallback argument will also support a function
\t"""
