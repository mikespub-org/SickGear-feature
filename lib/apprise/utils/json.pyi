import json
from ..common import AWARE_DATE_ISO_FORMAT as AWARE_DATE_ISO_FORMAT, NAIVE_DATE_ISO_FORMAT as NAIVE_DATE_ISO_FORMAT
from ..locale import LazyTranslation as LazyTranslation

class AppriseJSONEncoder(json.JSONEncoder):
    """A JSON Encoder for handling Apprise internals."""
    def default(self, entry): ...
