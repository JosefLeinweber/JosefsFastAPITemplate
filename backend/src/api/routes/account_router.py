import fastapi
import loguru
from sqlalchemy.ext.asyncio import (
    async_sessionmaker as sqlalchemy_async_sessionmaker,
    AsyncEngine as SQLAlchemyAsyncEngine,
    AsyncSession as SQLAlchemyAsyncSession,
    create_async_engine as create_sqlalchemy_async_engine,
)

from src.config.settings.setup import settings, Settings
from src.crud import account_crud
from src.models.schemas.account_schema import AccountInAuthentication, AccountInUpdate, AccountOut, AccountOutDelete
from src.utility.database.db_session import get_async_session

router = fastapi.APIRouter(prefix="/account", tags=["account"])


@router.post(
    path="",
    name="account:create_account",
    response_model=AccountOut,
    status_code=201,
)
async def create_account(
    new_account: AccountInAuthentication,
    db_session: SQLAlchemyAsyncSession = fastapi.Depends(get_async_session),
) -> AccountOut:
    try:
        created_account = await account_crud.create(new_account, db_session)
        return AccountOut(**created_account.__dict__)
    except fastapi.HTTPException as e:
        loguru.logger.debug(f"Error creating account: {e.detail}")
        raise e  # Re-raise the HTTPException so FastAPI can handle it
    except Exception as e:
        loguru.logger.error(f"Unexpected error: {e}")
        raise fastapi.HTTPException(status_code=500, detail="Internal server error")


@router.get(
    path="",
    name="account:get_all_accounts",
    response_model=list[AccountOut],
    status_code=200,
)
async def get_all_accounts(
    db_session: SQLAlchemyAsyncSession = fastapi.Depends(get_async_session),
) -> list[AccountOut]:

    accounts = await account_crud.get_all(db_session)
    if not accounts:
        raise fastapi.HTTPException(status_code=404, detail="No accounts found")
    return [AccountOut(**account.__dict__) for account in accounts]


@router.get(
    path="/{id}",
    name="account:get_account_by_id",
    response_model=AccountOut,
    status_code=200,
)
async def get_account_by_id(
    id: int,
    db_session: SQLAlchemyAsyncSession = fastapi.Depends(get_async_session),
) -> AccountOut:
    account = await account_crud.get_by_id(id, db_session)
    if not account:
        raise fastapi.HTTPException(status_code=404, detail="Account not found")
    return AccountOut(**account.__dict__)


@router.put(
    path="/{id}",
    name="account:update_account_by_id",
    response_model=AccountOut,
    status_code=200,
)
async def update_account_by_id(
    id: int,
    update_account: AccountInUpdate,
    db_session: SQLAlchemyAsyncSession = fastapi.Depends(get_async_session),
) -> AccountOut:
    account = await account_crud.update_by_id(id, update_account, db_session)
    if not account:
        raise fastapi.HTTPException(status_code=404, detail="Account not found")
    return AccountOut(**account.__dict__)


@router.delete(
    path="/{id}",
    name="account:delete_account_by_id",
    response_model=AccountOutDelete,
    status_code=200,
)
async def delete_account_by_id(
    id: int,
    db_session: SQLAlchemyAsyncSession = fastapi.Depends(get_async_session),
) -> fastapi.Response:
    is_deleted = await account_crud.delete_by_id(id, db_session)
    return AccountOutDelete(is_deleted=is_deleted)
