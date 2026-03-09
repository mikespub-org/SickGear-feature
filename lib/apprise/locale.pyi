import contextlib
from .logger import logger as logger
from _typeshed import Incomplete
from collections.abc import Generator

GETTEXT_LOADED: bool

class AppriseLocale:
    """A wrapper class to gettext so that we can manipulate multiple lanaguages
    on the fly if required."""
    _domain: str
    _locale_dir: Incomplete
    _local_re: Incomplete
    _default_encoding: str
    _fn: str
    _default_language: str
    _gtobjs: Incomplete
    lang: Incomplete
    __fn_map: Incomplete
    def __init__(self, language=None) -> None:
        """Initializes our object, if a language is specified, then we
        initialize ourselves to that, otherwise we use whatever we detect from
        the local operating system.

        If all else fails, we resort to the defined default_language.
        """
    def add(self, lang=None, set_default: bool = True):
        """Add a language to our list."""
    @contextlib.contextmanager
    def lang_at(self, lang, mapto=...) -> Generator[Incomplete]:
        """
        The syntax works as:
            with at.lang_at('fr'):
                # apprise works as though the french language has been
                # defined. afterwards, the language falls back to whatever
                # it was.
        """
    @property
    def gettext(self):
        """Return the current language gettext() function.

        Useful for assigning to `_`
        """
    @staticmethod
    def detect_language(lang=None, detect_fallback: bool = True):
        """Returns the language (if it's retrievable)"""
    def __getstate__(self):
        """Pickle Support dumps()"""
    def __setstate__(self, state) -> None:
        """Pickle Support loads()"""

LOCALE: Incomplete

class LazyTranslation:
    """Doesn't translate anything until str() or unicode() references are
    made."""
    text: Incomplete
    def __init__(self, text, *args, **kwargs) -> None:
        """Store our text."""
    def __str__(self) -> str: ...

def gettext_lazy(text):
    """A dummy function that can be referenced."""
Translatable = str | LazyTranslation
