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


@pytest.mark.asyncio
async def test_get_account_by_id_successful(async_client: AsyncClient):
    # GIVEN: An existing account in the database
    response = await async_client.post(
        "/v1/account", json={"username": "getById", "email": "getById@gmx.de", "password": "Test1234!"}
    )
    assert response.status_code == 201
    account_id = response.json()["id"]

    # WHEN: I try to get the account by its ID
    response = await async_client.get(f"/v1/account/{account_id}")

    # THEN: I should get a 200 OK response with the account details
    assert response.status_code == 200
    assert response.json()["id"] == account_id
    assert response.json()["username"] == "getById"
    assert response.json()["email"] == "getById@gmx.de"


@pytest.mark.asyncio
async def test_get_account_by_id_not_found(async_client: AsyncClient):
    # GIVEN: A non-existent account ID
    non_existent_id = 9999

    # WHEN: I try to get the account by its ID
    response = await async_client.get(f"/v1/account/{non_existent_id}")

    # THEN: I should get a 404 Not Found response
    assert response.status_code == 404
    assert response.json()["detail"] == "Account not found"


@pytest.mark.asyncio
async def test_update_account_by_id_successful(async_client: AsyncClient):
    # GIVEN: An existing account in the database
    response = await async_client.post(
        "/v1/account", json={"username": "updateTest", "email": "updateTest@gmx.de", "password": "Test1234!"}
    )
    assert response.status_code == 201
    account_id = response.json()["id"]

    # WHEN: I update the account's username and email
    update_data = {"username": "updatedUsername", "email": "updatedEmail@gmx.de"}
    response = await async_client.put(f"/v1/account/{account_id}", json=update_data)

    # THEN: I should get a 200 OK response with the updated account details
    assert response.status_code == 200
    assert response.json()["id"] == account_id
    assert response.json()["username"] == "updatedUsername"
    assert response.json()["email"] == "updatedEmail@gmx.de"


@pytest.mark.asyncio
async def test_update_account_by_id_not_found(async_client: AsyncClient):
    # GIVEN: A non-existent account ID
    non_existent_id = 9999

    # WHEN: I try to update the account
    update_data = {"username": "nonExistent", "email": "nonExistent@gmx.de"}
    response = await async_client.put(f"/v1/account/{non_existent_id}", json=update_data)

    # THEN: I should get a 404 Not Found response
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


@pytest.mark.asyncio
async def test_delete_account_by_id_successful(async_client: AsyncClient):
    # GIVEN: An existing account in the database
    response = await async_client.post(
        "/v1/account", json={"username": "deleteTest", "email": "deleteTest@gmx.de", "password": "Test1234!"}
    )
    assert response.status_code == 201
    account_id = response.json()["id"]

    # WHEN: I delete the account by its ID
    response = await async_client.delete(f"/v1/account/{account_id}")

    # THEN: I should get a 200 OK response with the deletion confirmation
    assert response.status_code == 200
    assert response.json()["isDeleted"] is True


@pytest.mark.asyncio
async def test_delete_account_by_id_not_found(async_client: AsyncClient):
    # GIVEN: A non-existent account ID
    non_existent_id = 9999

    # WHEN: I try to delete the account
    response = await async_client.delete(f"/v1/account/{non_existent_id}")

    # THEN: I should get a 404 Not Found response
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
    assert True == False  # force fail
