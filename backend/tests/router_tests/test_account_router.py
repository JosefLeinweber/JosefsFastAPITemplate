import loguru
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_all_accounts(async_client: AsyncClient):
    response = await async_client.get("/v1/account")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_account(async_client: AsyncClient):
    response = await async_client.post(
        "/v1/account",
        json={"username": "test", "email": "test@gmx.de", "password": "Test1234!"},
    )
    loguru.logger.debug(response.json())
    assert response.status_code == 201
    assert response.json()["username"] == "test"
    assert response.json()["email"] == "test@gmx.de"
    assert response.json()["password"] != "Test1234!"
    assert response.json()["id"] is not None
    assert response.json()["created_at"] is not None
    assert response.json()["isAdmin"] is False
    assert response.json()["isLoggedIn"] is True
    assert response.json()["isVerified"] is False
