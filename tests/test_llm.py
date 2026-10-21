from models.endpoint import DEFAULT_ENDPOINT_URL, normalize_endpoint_url
from models.llm.llm import LiquidLargeLanguageModel


def test_blank_endpoint_uses_default():
    assert normalize_endpoint_url({"endpoint_url": "  "}) == DEFAULT_ENDPOINT_URL
    assert normalize_endpoint_url({}) == DEFAULT_ENDPOINT_URL


def test_endpoint_loses_trailing_slash():
    assert normalize_endpoint_url({"endpoint_url": " https://x.test/v1/ "}) == "https://x.test/v1"


def test_credentials_get_attribution_headers():
    credentials = {"extra_headers": {"X-Other": "1"}}
    LiquidLargeLanguageModel._update_credential(None, credentials)
    assert credentials["extra_headers"] == {
        "X-Other": "1",
        "HTTP-Referer": "https://dify.ai/",
        "X-Title": "Dify",
    }
    assert credentials["endpoint_url"] == DEFAULT_ENDPOINT_URL
    assert credentials["mode"] == "chat"
