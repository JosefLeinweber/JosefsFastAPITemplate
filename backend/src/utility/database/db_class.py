import loguru
import pydantic
from sqlalchemy.ext.asyncio import (
    async_sessionmaker as sqlalchemy_async_sessionmaker,
    AsyncEngine as SQLAlchemyAsyncEngine,
    AsyncSession as SQLAlchemyAsyncSession,
    create_async_engine as create_sqlalchemy_async_engine,
)

from src.config.settings.setup import settings


class Database:
    """
    Database for:
        - Asynchronous SQLAlchemy
        - Asynchronous Postgres Server

        Functionalities:
            - create async engine
            - initialize async engine
            - initialize async session
    """

    def __init__(self):
        loguru.logger.info(f"DB Class: \t Initializing database...")
        self.server: str = "Asynchronous Postgres Server"
        self.framework: str = "Asynchronous SQLAlchemy"
        self._async_engine: SQLAlchemyAsyncEngine | None = None
        self._async_session: sqlalchemy_async_sessionmaker[SQLAlchemyAsyncSession] | None = None
        self.postgres_uri: str = (
            f"{settings.POSTGRES_SCHEMA}://{settings.POSTGRES_USERNAME}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        )

    @property
    def async_engine(self) -> SQLAlchemyAsyncEngine:
        if self._async_engine:
            return self._async_engine
        else:
            self.initialize_async_engine
        return self.async_engine

    @property
    def initialize_async_engine(self) -> None:
        loguru.logger.debug(f"DB Class: \t Initializing async engine...")
        loguru.logger.info(f"DB Class: \t Postgres URI: {self.postgres_uri}")
        self._async_engine = create_sqlalchemy_async_engine(
            url=self.postgres_uri,
            echo=settings.POSTGRES_ECHO,
            pool_size=settings.DB_POOL_SIZE,
            max_overflow=settings.DB_MAX_OVERFLOW,
        )

    @property
    def async_session(self) -> sqlalchemy_async_sessionmaker[SQLAlchemyAsyncSession]:
        if self._async_session:
            return self._async_session
        else:
            self.initialize_async_session
        return self.async_session

    @property
    def initialize_async_session(self) -> None:
        self._async_session = sqlalchemy_async_sessionmaker(bind=self.async_engine, expire_on_commit=False)

    def __call__(self):
        loguru.logger.info(f"DB Class: \t Database is called!")
        loguru.logger.info(f"Establishing SQLAlchemy Async Engine...")
        while not self.async_engine:
            loguru.logger.info(f"Initializing SQLAlchemy Async Engine...")
            self.initialize_async_engine()  # type: ignore
        loguru.logger.info(f"Successfully Initialized SQLAlchemy Async Engine!")

        while not self.async_session:
            loguru.logger.info(f"Initializing SQLAlchemy Async Session...")
            self.initialize_async_session()  # type: ignore
        loguru.logger.info(f"Successfully Initialized SQLAlchemy Async Session!")
        return self

    def __str__(self) -> str:
        return f"Database Server: {self.server} with {self.framework}"


def get_database() -> Database:
    return Database()


db = get_database()
