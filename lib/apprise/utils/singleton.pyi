from _typeshed import Incomplete

class Singleton(type):
    """Our Singleton MetaClass."""
    _instances: Incomplete
    def __call__(cls, *args, **kwargs):
        """Instantiate our singleton meta entry."""
