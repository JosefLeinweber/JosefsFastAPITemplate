"""
Get async session through function with proper lifecycle management.
"""

from typing import AsyncGenerator

import loguru
from sqlalchemy.ext.asyncio import AsyncSession

from src.utility.database.db_class import db


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency function to provide an async database session.
    Ensures proper session lifecycle management.
    """
    async with db.async_session() as session:
        try:
            yield session
        except Exception as exception:
            loguru.logger.error(f"Exception in async session: {exception}")
            await session.rollback()
            raise


# randomg
