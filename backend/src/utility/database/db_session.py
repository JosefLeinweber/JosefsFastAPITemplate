"""
get async sesison through function
"""

from typing import Generator

import loguru

from src.utility.database.db_class import db


async def get_async_session() -> Generator:  # type: ignore
    try:
        yield db.async_session
    except Exception as exception:
        loguru.logger.debug(f"Exception in async session: {exception}")
        await db.async_session().rollback()
        raise exception
    finally:
        await db.async_session().close()
