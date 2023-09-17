import json
from typing import Any

from redis.asyncio import Redis

from app.cache.cache import Cache
from redis import asyncio as aioredis

from app.config import conf


class AuthTokenCache(Cache):
    def __init__(self):
        self.redis_db: int = conf.redis.auth_token_db
        self.redis_password: str = conf.redis.auth_token_password
        self._connection: Redis | None = None

    async def connect(self):
        self._connection = aioredis.StrictRedis(
            db=self.redis_db,
            password=self.redis_password,
        )

    async def disconnect(self):
        await self._connection.close()
        self._connection = None

    async def get(self, key: str):
        value = await self._connection.get(key)
        if value is None:
            return None
        return json.loads(value)

    async def set(
        self,
        key: str,
        value: Any,
        expire: int = conf.auth.access_token_expire,
    ):
        data = json.dumps(value)
        await self._connection.setex(name=key, time=expire, value=data)

    async def update(
        self,
        key: str,
        value: Any,
        expire: int = conf.auth.access_token_expire,
    ):
        await self.set(key=key, value=value)

    async def delete(self, key: str):
        await self._connection.delete(key)
