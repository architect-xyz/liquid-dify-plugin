from dify_plugin import OAICompatLargeLanguageModel

from models.endpoint import normalize_endpoint_url

# The exchange reads X-Title as the name of the client on a buyer's receipts,
# and HTTP-Referer as the site of the caller.
ATTRIBUTION_HEADERS = {
    "HTTP-Referer": "https://dify.ai/",
    "X-Title": "Dify",
}


class LiquidLargeLanguageModel(OAICompatLargeLanguageModel):
    def _update_credential(self, credentials: dict) -> None:
        credentials["endpoint_url"] = normalize_endpoint_url(credentials)
        credentials["mode"] = "chat"
        credentials["extra_headers"] = {
            **credentials.get("extra_headers", {}),
            **ATTRIBUTION_HEADERS,
        }

    def _invoke(self, model, credentials, *args, **kwargs):
        self._update_credential(credentials)
        return super()._invoke(model, credentials, *args, **kwargs)

    def validate_credentials(self, model, credentials) -> None:
        self._update_credential(credentials)
        super().validate_credentials(model, credentials)

    def get_num_tokens(self, model, credentials, *args, **kwargs):
        self._update_credential(credentials)
        return super().get_num_tokens(model, credentials, *args, **kwargs)

    def get_customizable_model_schema(self, model, credentials):
        self._update_credential(credentials)
        return super().get_customizable_model_schema(model, credentials)
