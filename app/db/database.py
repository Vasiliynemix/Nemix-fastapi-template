from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import (
    create_async_engine as _create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from app.config import conf
from app.db.models import User


def create_async_engine():
    return _create_async_engine(url=conf.db.build_connection_str(), echo=conf.db.debug)


async_session_maker = async_sessionmaker(
    bind=create_async_engine(), expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User) # noqa
