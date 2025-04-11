import fastapi
import loguru
import sqlalchemy
from sqlalchemy import exc as sqlalchemy_error
from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession
from sqlalchemy.orm import selectinload as sqlalchemy_selectinload
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db_tables.account_table import Account
from src.models.schemas.account_schema import AccountInAuthentication, AccountInUpdate, AccountOut, AccountOutDelete


async def create(account: AccountInAuthentication, db_session: SQLAlchemyAsyncSession) -> Account:
    loguru.logger.info("* creating new account")
    # TODO: dict() is DeprecationWarning
    new_account = Account(**account.model_dump())
    try:
        await _check_account_details_are_unique(account=account, db_session=db_session)
        db_session.add(instance=new_account)
        await db_session.commit()
        await db_session.refresh(instance=new_account)
        return new_account
    except fastapi.HTTPException as exception:
        raise exception

    except sqlalchemy_error.DatabaseError as e:
        await db_session.rollback()
        loguru.logger.error(f"Error creating account: {e}")
        raise fastapi.HTTPException(status_code=500, detail=str(e))


async def get_all(db_session: SQLAlchemyAsyncSession) -> list[AccountOut]:
    loguru.logger.info("* fetching all accounts")
    select_stmt = sqlalchemy.select(Account).options(sqlalchemy_selectinload("*"))

    try:
        query = await db_session.execute(statement=select_stmt)
        return query.scalars().all()

    except sqlalchemy_error.DatabaseError as e:
        loguru.logger.error(f"Error getting all accounts: {e}")
        raise fastapi.HTTPException(status_code=500, detail=str(e))


async def get_by_id(id: int, db_session: SQLAlchemyAsyncSession) -> AccountOut:
    loguru.logger.info("* fetching account by id")
    select_stmt = sqlalchemy.select(Account).options(sqlalchemy_selectinload("*")).where(Account.id == id)
    try:
        query = await db_session.execute(statement=select_stmt)
        return query.scalars().first()

    except sqlalchemy_error.DatabaseError as e:
        loguru.logger.error(f"Error getting account by id: {e}")
        raise fastapi.HTTPException(status_code=500, detail=str(e))


async def update_by_id(id: int, account: AccountInUpdate, db_session: SQLAlchemyAsyncSession) -> AccountOut:
    loguru.logger.info("* updating account by id")
    update_data = account.dict(exclude_unset=True)

    current_account = await get_by_id(id=id, db_session=db_session)
    if not current_account:
        raise fastapi.HTTPException(status_code=404, detail=f"Account with id {id} not found")

    update_stmt = sqlalchemy.update(Account).where(Account.id == id).values(updated_at=sqlalchemy_functions.now())

    for key, value in update_data.items():
        update_stmt = update_stmt.values(**{key: value})

    try:
        await db_session.execute(statement=update_stmt)
        await db_session.commit()
        await db_session.close()

        return await get_by_id(id=id, db_session=db_session)

    except sqlalchemy_error.DatabaseError as e:
        await db_session.rollback()
        await db_session.close()
        raise fastapi.HTTPException(status_code=500, detail=str(e))


async def delete_by_id(id: int, db_session: SQLAlchemyAsyncSession) -> bool:
    loguru.logger.info("* deleting account by id")
    accout_to_delete = await get_by_id(id=id, db_session=db_session)
    if not accout_to_delete:
        raise fastapi.HTTPException(status_code=404, detail=f"Account with id {id} not found")
    delete_stmt = sqlalchemy.delete(Account).where(Account.id == id)
    try:
        await db_session.execute(statement=delete_stmt)
        await db_session.commit()
        await db_session.close()
        return True
    except sqlalchemy_error.DatabaseError as e:
        await db_session.rollback()
        await db_session.close()
        raise fastapi.HTTPException(status_code=500, detail=str(e))


async def _check_account_details_are_unique(
    account: AccountInAuthentication, db_session: SQLAlchemyAsyncSession
) -> None:
    loguru.logger.info("* checking if account details are unique")
    email_unique = await _is_email_unique(account.email, db_session)
    username_unique = await _is_username_unique(account.username, db_session)
    if not email_unique:
        raise fastapi.HTTPException(status_code=409, detail=f"Email {account.email} already in use")
    if not username_unique:
        raise fastapi.HTTPException(status_code=409, detail=f"Username {account.username} already in use")


async def _is_email_unique(email: str, db_session: SQLAlchemyAsyncSession) -> bool:
    loguru.logger.info("* checking if email is unique")
    select_stmt = sqlalchemy.select(Account).where(Account.email == email)
    query = await db_session.execute(statement=select_stmt)
    return query.scalars().first() is None


async def _is_username_unique(username: str, db_session: SQLAlchemyAsyncSession) -> bool:
    loguru.logger.info("* checking if username is unique")
    select_stmt = sqlalchemy.select(Account).where(Account.username == username)
    query = await db_session.execute(statement=select_stmt)
    return query.scalars().first() is None
