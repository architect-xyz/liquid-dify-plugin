import logging

from dify_plugin import ModelProvider
from dify_plugin.entities.model import ModelType
from dify_plugin.errors.model import CredentialsValidateFailedError

logger = logging.getLogger(__name__)

VALIDATION_MODEL = "liquid.auto"


class LiquidProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        try:
            self.get_model_instance(ModelType.LLM).validate_credentials(
                model=VALIDATION_MODEL, credentials=credentials
            )
        except CredentialsValidateFailedError:
            raise
        except Exception:
            logger.exception("liquid credentials validation failed")
            raise
