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

    async def add(self, data: dict) -> type(model):
        stmt = insert(self.model).values(**data)
        return await self.session.scalar(stmt)

    async def get(self, ident: int) -> type(model):
        return self.session.get(entity=self.model, ident=ident)

    async def update(self, values: dict) -> type(model):
        stmt = update(self.model).values(**values).returning(self.model)
        return await self.session.scalar(stmt)

    async def delete(self, ident: int):
        stmt = delete(self.model).where(self.model.id == ident)
        await self.session.scalar(stmt)

    async def find_all(self) -> list[type(model)]:
        stmt = select(self.model)
        result = await self.session.scalars(stmt)
        return list(result.all())
