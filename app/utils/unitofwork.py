from abc import ABC, abstractmethod

from app.db.database import async_session_maker
from app.db.repositories.tasks import TasksRepository
from app.db.repositories.users import UsersRepository


class IUnitOfWork(ABC):
    users: type[UsersRepository]
    tasks: type[TasksRepository]

    @abstractmethod
    def __init__(self):
        raise NotImplementedError
    
    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker
        self.model = None

    async def __aenter__(self):
        self.session = self.session_factory()

        self.tasks = TasksRepository(session=self.session) # noqa
        self.users = UsersRepository(session=self.session) # noqa

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
