from src.config.settings.base import Settings

# Use a secret manager to store sensitive information in production


class ProductionSettings(Settings):
    DESCRIPTION: str = "Production Settings | Modified FastAPI Template"
    DEBUG: bool = False
    TESTING: bool = False
