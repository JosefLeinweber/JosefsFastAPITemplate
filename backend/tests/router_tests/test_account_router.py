import loguru
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_all_accounts(async_client: AsyncClient):
    # GIVEN: An existing account in the database
    response = await async_client.post(
        "/v1/account", json={"username": "tgaa", "email": "tgaa@gnx.de", "password": "Test1234!"}
    )
    assert response.status_code == 201
    # WHEN: I try to get all accounts
    response = await async_client.get("/v1/account")

    # THEN: I should get a 200 OK response with a list of accounts
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_create_account_successful(async_client: AsyncClient):
    # GIVEN: I have a valid account creation request
    # WHEN: I send the request to create a new account
    response = await async_client.post(
        "/v1/account",
        json={"username": "test", "email": "test@gmx.de", "password": "Test1234!"},
    )
    # THEN: I should get a 201 Created response with the account details
    loguru.logger.debug(response.json())
    assert response.status_code is 201
    assert response.json()["username"] == "test"
    assert response.json()["email"] == "test@gmx.de"
    assert response.json()["id"] is not None
    assert response.json()["createdAt"] is not None
    assert response.json()["isAdmin"] is False
    assert response.json()["isLoggedIn"] is True
    assert response.json()["isVerified"] is False


@pytest.mark.asyncio
async def test_create_account_username_must_be_unique(async_client: AsyncClient):
    # GIVEN: an existing account with username "notUnique"
    first_response = await async_client.post(
        "/v1/account", json={"username": "notUnique", "email": "test123@gnx.de", "password": "Test1234!"}
    )
    assert first_response.status_code == 201
    # WHEN: I try to create a new account with the same username
    response = await async_client.post(
        "/v1/account",
        json={"username": "notUnique", "email": "test1@gnx.de", "password": "Test1234!"},  # username already exists
    )
    # THEN: I should get a 409 Conflict response
    assert response.status_code == 409


@pytest.mark.asyncio
async def test_create_account_invalid_email(async_client: AsyncClient):
    # GIVEN: an existing account with email "notUnique@gmx.de"
    first_response = await async_client.post(
        "/v1/account", json={"username": "tcaie", "email": "notUnique@gmx.de", "password": "Test1234!"}
    )
    # WHEN: I try to create an account with that email address
    response = await async_client.post(
        "/v1/account",
        json={"username": "tcaie1", "email": "notUnique@gmx.de", "password": "Test1234!"},  # email already exists
    )
    loguru.logger.debug(response.json())
    # THEN: I should get a 409 Conflict response
    assert response.status_code == 409
