from abc import ABC, abstractmethod

from sqlalchemy import insert, update, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import Base


class AbstractRepository(ABC):
    @abstractmethod
    async def add(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get(self, ident: int):
        raise NotImplementedError

    @abstractmethod
    async def update(self, values: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, ident: int):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model: type[Base] = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        return await self.session.scalar(stmt)

    async def get(self, ident: int):
        stmt = select(self.model).where(self.model.id == ident)
        return await self.session.scalar(stmt)

    async def update(self, values: dict):
        stmt = update(self.model).values(**values).returning(self.model)
        return await self.session.scalar(stmt)

    async def delete(self, ident: int):
        stmt = delete(self.model).where(self.model.id == ident)
        await self.session.scalar(stmt)

    async def find_all(self):
        stmt = select(self.model).order_by(self.model.update_at)
        models = await self.session.scalars(stmt)
        return models.all()
