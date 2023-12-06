import asyncio

import asgi_lifespan
import pytest
from httpx import AsyncClient

from src.main import initialize_application


@pytest.fixture(scope="function")
def event_loop():
    """Overrides pytest default function scoped event loop"""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def async_client():
    async with AsyncClient(app=initialize_application(), base_url="http://test") as async_client:
        print("Client is ready")
        yield async_client
