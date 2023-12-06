import asyncio
import os

import pytest
from httpx import AsyncClient

from src.main import initialize_application

os.environ["ENVIRONMENT"] = "STAGING"


@pytest.fixture(scope="session")
def event_loop():
    """Overrides pytest default function scoped event loop"""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
def initalize_test_app():
    try:
        test_app = initialize_application()
        return test_app
    except Exception as e:
        raise e


@pytest.fixture(scope="session")
@pytest.mark.asyncio
async def async_client(event_loop, initalize_test_app) -> AsyncClient:
    async with AsyncClient(app=initalize_test_app, base_url="http://test") as async_client:
        print("Client is ready")
        yield async_client
