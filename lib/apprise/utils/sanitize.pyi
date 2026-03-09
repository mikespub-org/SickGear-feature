from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any

_BLOB_KEYWORDS: Incomplete

@dataclass(frozen=True)
class SanitizeOptions:
    """Options controlling payload sanitization for debug logging.

    The defaults are deliberately conservative and tuned for logging, not for
    data processing. When in doubt, prefer smaller values to keep logging
    cheap.

    Attributes:
        max_depth: Maximum recursion depth before truncation markers appear.
        max_items: Global upper bound on visited items, across the whole walk.
        max_str_len: Strings longer than this are summarized with a preview.
        preview: Number of characters to show at the start and end of
                 summaries.
        hash_sample_size: Maximum bytes hashed when generating a sha256
                          preview.
        aggressive_blob_keys: If True, summarize values under blob-like keys
            even when they are not huge, because these values are often encoded
            attachments (for example, base64).
    """
    max_depth: int = ...
    max_items: int = ...
    max_str_len: int = ...
    preview: int = ...
    hash_sample_size: int = ...
    aggressive_blob_keys: bool = ...

def sanitize_payload(value: Any, *, options: SanitizeOptions | None = None) -> Any:
    '''
    This function is intended for DEBUG and TRACE logging only.

    can add i/o to generate the printed copy, but the output is much
    better then just printing what could be a massive payload (with
    attachments).

    The ideal setup for this function is when you need to print what
    could be a very large object such as in the send() of a Apprise
    service, you would structure it like this:

        # check for at least the DEBUG level... you can also set
        # logging.TRACE if you wanted as well:
        if self.logger.isEnabledFor(logging.DEBUG):

            # Then safely wrap the output using this function:
            self.logger.debug(
                "Service Payload: %s", sanitize_payload(payload))
    '''
