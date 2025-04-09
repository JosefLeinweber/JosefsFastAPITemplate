import decouple

from src.config.settings.base import Settings


class StagingSettings(Settings):
    DESCRIPTION: str = "Staging / Testing Settings | Modified FastAPI Template"
    DEBUG: bool = True
    TESTING: bool = True
    POSTGRES_DB: str = decouple.config("POSTGRES_TEST_DB", cast=str)  # type: ignore
    POSTGRES_HOST: str = decouple.config("POSTGRES_TEST_HOST", cast=str)  # type: ignore
