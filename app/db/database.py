from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import conf

engine = create_async_engine(url=conf.db.build_connection_str(), echo=True)
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
