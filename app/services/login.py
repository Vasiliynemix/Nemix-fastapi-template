from datetime import timedelta

from fastapi import HTTPException
from starlette import status

from app.api.v1.dependencies import UOWDep
from app.api.v1.response import ErrorResponse
from app.config import conf
from app.schemas.login import Token
from app.security.access_token import create_access_token
from app.security.hashed_password import PasswordCheck
from app.utils.decorators import WithUOWDecorator


class LoginService(metaclass=WithUOWDecorator):
    async def get_user_by_username_in_depends( # noqa
        self,
        username: str,
        uow: UOWDep,
    ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=await ErrorResponse(
                status_code=401,
                message=f"Could not validate credentials",
            ).to_dict_one(),
        )
        user = await uow.users.get_user_by_username(
            username=username
        )
        if user is None:
            return credentials_exception

        return user

    async def authenticate_user(  # noqa
        self,
        uow: UOWDep,
        password: str,
        username: str,
    ):
        incorrect_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=await ErrorResponse(
                status_code=401,
                message=f"incorrect username or email",
            ).to_dict_one(),
        )

        user = await uow.users.get_user_by_username(username=username)
        if user is None:
            raise incorrect_exception

        password = PasswordCheck(password=password)
        if not await password.verify_password(user.hashed_password):
            raise incorrect_exception
        return user

    async def create_token_for_username(self, user):  # noqa
        access_token_expires = timedelta(minutes=conf.auth.access_token_expires)
        access_token = create_access_token(
            data={"sub": user.username, "user_id": user.id},
            expires_delta=access_token_expires,
        )
        token = Token(access_token=access_token, token_type="bearer")
        return token
