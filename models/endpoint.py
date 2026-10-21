DEFAULT_ENDPOINT_URL = "https://router.inference.ai.exchange/v1"


def normalize_endpoint_url(credentials: dict) -> str:
    """Return the API base URL without spaces or a trailing slash."""
    endpoint_url = (credentials.get("endpoint_url") or "").strip().rstrip("/")
    return endpoint_url or DEFAULT_ENDPOINT_URL
