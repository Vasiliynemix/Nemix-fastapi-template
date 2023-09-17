from app.cache.auth_token import AuthTokenCache


async def get_redis():
    redis_client = AuthTokenCache()
    await redis_client.connect()
    yield redis_client
    await redis_client.disconnect()
