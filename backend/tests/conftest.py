import pytest
from httpx import AsyncClient

from src.config.settings.setup import settings


@pytest.fixture
async def async_client():
    app_url = f"http://{settings.SERVER_HOST}:{settings.SERVER_PORT}"
    async with AsyncClient(base_url=app_url) as async_client:
        yield async_client
