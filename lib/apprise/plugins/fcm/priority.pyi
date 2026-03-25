from ...logger import logger as logger
from .common import FCMMode as FCMMode, FCM_MODES as FCM_MODES
from _typeshed import Incomplete

class NotificationPriority:
    """
    Defines the Notification Priorities as described on:
    https://firebase.google.com/docs/reference/fcm/rest/v1/            projects.messages#androidmessagepriority

        NORMAL:
            Default priority for data messages. Normal priority messages won't
            open network connections on a sleeping device, and their delivery
            may be delayed to conserve the battery. For less time-sensitive
            messages, such as notifications of new email or other data to sync,
            choose normal delivery priority.

        HIGH:
            Default priority for notification messages. FCM attempts to
            deliver high priority messages immediately, allowing the FCM
            service to wake a sleeping device when possible and open a network
            connection to your app server. Apps with instant messaging, chat,
            or voice call alerts, for example, generally need to open a
            network connection and make sure FCM delivers the message to the
            device without delay. Set high priority if the message is
            time-critical and requires the user's immediate interaction, but
            beware that setting your messages to high priority contributes
            more to battery drain compared with normal priority messages.
    """
    NORMAL: str
    HIGH: str

class FCMPriority:
    """Defines our accepted priorites."""
    MIN: str
    LOW: str
    NORMAL: str
    HIGH: str
    MAX: str

FCM_PRIORITIES: Incomplete

class FCMPriorityManager:
    """A Simple object to make it easier to work with FCM set priorities."""
    priority_map: Incomplete
    mode: Incomplete
    priority: Incomplete
    def __init__(self, mode, priority=None) -> None:
        """Takes a FCMMode and Priority."""
    def payload(self):
        """Returns our payload depending on our mode."""
    def __str__(self) -> str:
        """Our priority representation."""
    def __bool__(self) -> bool:
        """Allows this object to be wrapped in an 'if statement'.

        True is returned if a priority was loaded
        """
