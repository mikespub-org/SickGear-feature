from .logger import logger as logger
from .utils.disk import path_decode as path_decode
from .utils.module import import_module as import_module
from .utils.parse import parse_list as parse_list
from .utils.singleton import Singleton as Singleton
from _typeshed import Incomplete
from collections.abc import Generator

class PluginManager(metaclass=Singleton):
    """Designed to be a singleton object to maintain all initialized loading of
    modules in memory."""
    name: str
    _id: str
    module_name_prefix: Incomplete
    module_path: Incomplete
    module_filter_re: Incomplete
    _lock: Incomplete
    _module_map: Incomplete
    _schema_map: Incomplete
    _custom_module_map: Incomplete
    _disabled: Incomplete
    _paths_previously_scanned: Incomplete
    _loaded: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Over-ride our class instantiation to provide a singleton."""
    def unload_modules(self, disable_native: bool = False) -> None:
        """Reset our object and unload all modules."""
    def load_modules(self, path=None, name=None, force: bool = False) -> None:
        """Load our modules into memory."""
    def module_detection(self, paths, cache: bool = True) -> None:
        """Leverage the @notify decorator and load all objects found matching
        this."""
    def add(self, plugin, schemas=None, url=None, send_func=None, force: bool = False):
        """Ability to manually add Notification services to our stack."""
    def remove(self, *schemas, unload: bool = True) -> None:
        """Removes a loaded element (if defined)"""
    def plugins(self, include_disabled: bool = True) -> Generator[Incomplete]:
        """Return all of our loaded plugins."""
    def schemas(self, include_disabled: bool = True):
        """Return all of our loaded schemas.

        if include_disabled == True, then even disabled notifications are
        returned
        """
    def disable(self, *schemas) -> None:
        """Disables the modules associated with the specified schemas."""
    def enable_only(self, *schemas) -> None:
        """Disables the modules associated with the specified schemas."""
    def __contains__(self, schema) -> bool:
        """Checks if a schema exists."""
    def __delitem__(self, schema) -> None:
        """
        removes schema map and also unloads it from memory
        """
    def __setitem__(self, schema, plugin) -> None:
        """Support fast assigning of Plugin/Notification Objects."""
    def _unmap_schema(self, schema, *, unload: bool = True) -> None:
        """Unmap a schema entry without necessarily unloading modules.

        This function removes the schema mapping and updates internal cross
        references. When unload is True (default), modules are removed from
        sys.modules when they are no longer referenced by Apprise. When unload
        is False, the unmapping is performed but any imported modules remain
        intact in sys.modules.
        """
    def __getitem__(self, schema):
        """Returns the indexed plugin identified by the schema specified."""
    def __iter__(self):
        """Returns an iterator so we can iterate over our loaded modules."""
    def __len__(self) -> int:
        """Returns the number of modules/plugins loaded."""
    def __bool__(self) -> bool:
        """Determines if object has loaded or not."""
