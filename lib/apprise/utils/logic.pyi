from .. import common as common
from .parse import parse_list as parse_list

def is_exclusive_match(logic, data, match_all=..., match_always=...):
    '''The data variable should always be a set of strings that the logic can
    be compared against. It should be a set.  If it isn\'t already, then it will
    be converted as such. These identify the tags themselves.

    Our logic should be a list as well:
      - top level entries are treated as an \'or\'
      - second level (or more) entries are treated as \'and\'

      examples:
        logic="tagA, tagB"                = tagA or tagB
        logic=[\'tagA\', \'tagB\']            = tagA or tagB
        logic=[(\'tagA\', \'tagC\'), \'tagB\']  = (tagA and tagC) or tagB
        logic=[(\'tagB\', \'tagC\')]          = tagB and tagC

    If `match_always` is not set to None, then its value is added as an \'or\'
    to all specified logic searches.
    '''
def dict_full_update(dict1, dict2) -> None:
    """Takes 2 dictionaries (dict1 and dict2) that contain sub-dictionaries and
    gracefully merges them into dict1.

    This is similar to: dict1.update(dict2) except that internal dictionaries
    are also recursively applied.
    """
