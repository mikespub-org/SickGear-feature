import builtins
import hashlib
import json
from . import exception as exception
from .common import PersistentStoreMode as PersistentStoreMode
from .logger import logger as logger
from .utils.disk import path_decode as path_decode
from _typeshed import Incomplete
from datetime import datetime
from typing import Any

EPOCH: Incomplete
AWARE_DATE_ISO_FORMAT: str
NAIVE_DATE_ISO_FORMAT: str

def _ntf_tidy(ntf) -> None:
    """Reusable NamedTemporaryFile Cleanup."""

class CacheObject:
    hash_engine = hashlib.sha256
    hash_length: int
    __value: Incomplete
    __class_name: Incomplete
    __expires: Incomplete
    __persistent: Incomplete
    def __init__(self, value: Any = None, expires: bool | float | int | datetime | None = False, persistent: bool = True) -> None:
        """Tracks our objects and associates a time limit with them."""
    def set(self, value: Any, expires: bool | float | int | datetime | None = None, persistent: bool | None = None) -> None:
        """Sets fields on demand, if set to none, then they are left as is.

        The intent of set is that it allows you to set a new a value and
        optionally alter meta information against it.

        If expires or persistent isn't specified then their previous values are
        used.
        """
    def set_expiry(self, expires: datetime | bool | float | int | None = None) -> None:
        """Sets a new expiry."""
    def hash(self) -> str:
        """Our checksum to track the validity of our data."""
    def json(self) -> dict[str, Any] | None:
        """Returns our preparable json object."""
    @staticmethod
    def instantiate(content: dict[str, Any], persistent: bool = True, verify: bool = True) -> CacheObject | None:
        """Loads back data read in and returns a CacheObject or None if it
        could not be loaded.

        You can pass in the contents of CacheObject.json() and you'll receive a
        copy assuming the hash checks okay
        """
    @property
    def value(self) -> Any:
        """Returns our value."""
    @property
    def persistent(self) -> bool:
        """Returns our persistent value."""
    @property
    def expires(self) -> datetime | None:
        """Returns the datetime the object will expire."""
    @property
    def expires_sec(self) -> float | None:
        """Returns the number of seconds from now the object will expire."""
    def __bool__(self) -> bool:
        """Returns True it the object hasn't expired, and False if it has."""
    def __eq__(self, other) -> bool:
        """Handles equality == flag."""
    def __str__(self) -> str:
        """String output of our data."""

class CacheJSONEncoder(json.JSONEncoder):
    """A JSON Encoder for handling each of our cache objects."""
    def default(self, entry): ...

class PersistentStore:
    """An object to make working with persistent storage easier.

    read() and write() are used for direct file i/o

    set(), get() are used for caching
    """
    max_file_size: int
    default_file_expiry: int
    encoding: str
    base_key: str
    __cache_key: str
    temp_dir: str
    data_dir: str
    __extension: str
    __backup_extension: str
    __valid_key: Incomplete
    __not_found_ref: Incomplete
    __mode: Incomplete
    __exclude_list: Incomplete
    __renew: Incomplete
    __base_path: Incomplete
    __temp_path: Incomplete
    __data_path: Incomplete
    __dirty: bool
    __cache_size: Incomplete
    __cache_files: Incomplete
    _cache: Incomplete
    def __init__(self, path: str | None = None, namespace: str = 'default', mode: str | PersistentStoreMode | None = None) -> None:
        """Provide the namespace to work within.

        namespaces can only contain alpha-numeric characters with the exception
        of '-' (dash), '_' (underscore), and '.' (period). The namespace must
        be be relative to the current URL being controlled.
        """
    def read(self, key: str | None = None, compress: bool = True, expires: bool | float | int = False) -> bytes | None:
        """Returns the content of the persistent store object.

        if refresh is set to True, then the file's modify time is updated
        preventing it from getting caught in prune calls.  It's a means of
        allowing it to persist and not get cleaned up in later prune calls.

        Content is always returned as a byte object
        """
    def write(self, data: bytes | str | Any, key: str | None = None, compress: bool = True, _recovery: bool = False) -> bool:
        """Writes the content to the persistent store if it doesn't exceed our
        filesize limit.

        Content is always written as a byte object

        _recovery is reserved for internal usage and should not be changed
        """
    def __move(self, src, dst):
        """Moves the new file in place and handles the old if it exists already
        If the transaction fails in any way, the old file is swapped back.

        Function returns True if successful and False if not.
        """
    def open(self, key: str | None = None, mode: str = 'r', buffering: int = -1, encoding: str | None = None, errors: str | None = None, newline: str | None = None, closefd: bool = True, opener: Any | None = None, compress: bool = False, compresslevel: int = 9) -> Any:
        """Returns an iterator to our our file within our namespace identified
        by the key provided.

        If no key is provided, then the default is used
        """
    def get(self, key: str, default: Any = None, lazy: bool = True) -> Any:
        """Fetches from cache."""
    def set(self, key: str, value: Any, expires: float | int | datetime | bool | None = None, persistent: bool = True, lazy: bool = True) -> bool:
        """Cache reference."""
    def clear(self, *args: str) -> bool | None:
        """Remove one or more cache entry by it's key.

            e.g: clear('key')
                 clear('key1', 'key2', key-12')

        Or clear everything:
                 clear()
        """
    def prune(self) -> bool:
        """Eliminates expired cache entries."""
    def __load_cache(self, _recovery: bool = False):
        """Loads our cache.

        _recovery is reserved for internal usage and should not be changed
        """
    def __prepare(self, flush: bool = True):
        """Prepares a working environment."""
    def flush(self, force: bool = False, _recovery: bool = False) -> bool:
        """Save's our cache to disk."""
    def files(self, exclude: bool = True, lazy: bool = True) -> list[str]:
        """Returns the total files."""
    @staticmethod
    def disk_scan(path: str, namespace: str | list[str] | None = None, closest: bool = True) -> list[str]:
        """Scansk a path provided and returns namespaces detected."""
    @staticmethod
    def disk_prune(path: str, namespace: str | list[str] | None = None, expires: int | float | None = None, action: bool = False) -> dict[str, list[dict[str, str | bool]]]:
        """Prune persistent disk storage entries that are old and/or
        unreferenced.

        you must specify a path to perform the prune within

        if one or more namespaces are provided, then pruning focuses ONLY on
        those entries (if matched).

        if action is not set to False, directories to be removed are returned
        only
        """
    def size(self, exclude: bool = True, lazy: bool = True) -> int:
        """Returns the total size of the persistent storage in bytes."""
    def __del__(self) -> None:
        """Deconstruction of our object."""
    def __delitem__(self, key: str) -> None:
        """Remove a cache entry by it's key."""
    def __contains__(self, key: str) -> bool:
        """Verify if our storage contains the key specified or not.

        In additiont to this, if the content is expired, it is considered to be
        not contained in the storage.
        """
    def __setitem__(self, key: str, value: Any) -> None:
        """Sets a cache value without disrupting existing settings in place."""
    def __getitem__(self, key: str) -> Any:
        """Returns the indexed value."""
    def keys(self) -> builtins.set[str]:
        """Returns our keys."""
    def delete(self, *args: str, all: bool | None = None, temp: bool | None = None, cache: bool | None = None, validate: bool = True) -> bool:
        """Manages our file space and tidys it up.

        delete('key', 'key2') delete(all=True) delete(temp=True, cache=True)
        """
    @property
    def cache_file(self) -> str:
        """Returns the full path to the namespace directory."""
    @property
    def path(self) -> str | None:
        """Returns the full path to the namespace directory."""
    @property
    def mode(self) -> PersistentStoreMode:
        """Returns the Persistent Storage mode."""
