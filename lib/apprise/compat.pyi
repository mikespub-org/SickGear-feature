from typing import Any, Callable, TypeVar

_T = TypeVar('_T')

def dataclass_compat(*dargs: Any, **dkwargs: Any) -> Callable[[_T], _T]:
    """
    dataclass() wrapper that drops unsupported kwargs on older Python.

    Python 3.9 does not support slots= in dataclasses.dataclass().
    """
