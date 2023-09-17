from sqlalchemy.ext.asyncio import (
    create_async_engine as _create_async_engine,
    async_sessionmaker,
)

from app.config import conf


def create_async_engine():
    return _create_async_engine(url=conf.db.build_connection_str(), echo=conf.db.debug)


async_session_maker = async_sessionmaker(
    bind=create_async_engine(), expire_on_commit=False
)
