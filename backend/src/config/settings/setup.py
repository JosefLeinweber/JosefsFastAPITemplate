from functools import lru_cache

import decouple
import loguru

from src.config.settings.base import Settings
from src.config.settings.development import DevelopmentSettings
from src.config.settings.production import ProductionSettings
from src.config.settings.staging import StagingSettings


class SettingsFactory:
    def __init__(self, environment: str):
        self.environment = environment
        loguru.logger.debug(f"SettingsFactory initialized with environment: {self.environment}")

    def __call__(self) -> Settings:
        if self.environment == "DEV":
            return DevelopmentSettings()

        if self.environment == "PROD":
            return ProductionSettings()

        if self.environment == "STAGING":
            return StagingSettings()

        else:
            raise ValueError(f"Invalid environment: {self.environment}")


@lru_cache()
def get_settings() -> Settings:
    return SettingsFactory(environment=decouple.config("ENVIRONMENT", default="dev", cast=str))()


settings: Settings = get_settings()
