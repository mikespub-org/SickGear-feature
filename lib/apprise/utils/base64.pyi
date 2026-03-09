def base64_urlencode(data: bytes) -> str:
    """URL Safe Base64 Encoding."""
def base64_urldecode(data: str) -> bytes:
    """URL Safe Base64 Encoding."""
def decode_b64_dict(di: dict) -> dict:
    """Decodes base64 dictionary previously encoded.

    string entries prefixed with `b64:` are targeted
    """
def encode_b64_dict(di: dict, encoding: str = 'utf-8') -> tuple[dict, bool]:
    """Encodes dictionary entries containing binary types (int, float) into
    base64.

    Final product is always string based values
    """
