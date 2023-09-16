import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from app.api.v1 import routers
from app.api.v1.auth.auth import get_user_manager
from app.api.v1.auth.jwt import auth_backend
from app.api.v1.auth.schemas import UserRead, UserCreate, UserUpdate
from app.db.models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.__main__:app", reload=True)
