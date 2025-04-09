import os
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
    environment = os.getenv("ENVIRONMENT", "null").upper()
    loguru.logger.debug(f"Environment: {environment}")
    return SettingsFactory(environment)()


settings: Settings = get_settings()
