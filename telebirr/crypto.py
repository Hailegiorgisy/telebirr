import hashlib
import hmac

def sign_payload(payload_str: str, app_key: str) -> str:
    """Computes HMAC-SHA256 signature for Telebirr payment payload verification."""
    return hmac.new(app_key.encode("utf-8"), payload_str.encode("utf-8"), hashlib.sha256).hexdigest()
