import decouple

from src.config.settings.base import Settings


class DevelopmentSettings(Settings):
    DESCRIPTION: str = "Development Settings | Modified FastAPI Template"
    ENVIRONMENT: str = "dev"
    DEBUG: bool = True
    POSTGRES_DB: str = decouple.config("POSTGRES_DEV_DB", cast=str)  # type: ignore
    POSTGRES_HOST: str = decouple.config("POSTGRES_DEV_HOST", cast=str)  # type: ignore
