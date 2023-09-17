from abc import ABC, abstractmethod
from typing import Any

from app.config import conf


class Cache(ABC):
    @abstractmethod
    async def connect(self):
        raise NotImplementedError

    @abstractmethod
    async def disconnect(self):
        raise NotImplementedError

    @abstractmethod
    async def get(self, key: str):
        raise NotImplementedError

    @abstractmethod
    async def set(
        self,
        key: str,
        value: Any,
        expire: int = conf.auth.access_token_expire,
    ):
        raise NotImplementedError

    @abstractmethod
    async def update(
        self,
        key: str,
        value: Any,
        expire: int = conf.auth.access_token_expire,
    ):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, key: str):
        raise NotImplementedError
