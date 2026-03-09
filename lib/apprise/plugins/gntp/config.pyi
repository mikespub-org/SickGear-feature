from . import notifier

__all__ = ['mini', 'GrowlNotifier']

class GrowlNotifier(notifier.GrowlNotifier):
    """
\tConfigParser enhanced GrowlNotifier object

\tFor right now, we are only interested in letting users overide certain
\tvalues from ~/.gntp

\t::

\t\t[gntp]
\t\thostname = ?
\t\tpassword = ?
\t\tport = ?
\t"""
    def __init__(self, *args, **kwargs) -> None: ...

def mini(description, **kwargs) -> None:
    """Single notification function

\tSimple notification function in one line. Has only one required parameter
\tand attempts to use reasonable defaults for everything else
\t:param string description: Notification message
\t"""
