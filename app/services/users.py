from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from starlette import status

from app.api.v1.response import ErrorResponse
from app.schemas.users import UserAddSchema, UserUpdateSchema
from app.security.hashed_password import PasswordCheck
from app.utils.decorators import WithUOWDecorator
from app.utils.unitofwork import UnitOfWork


class UserService(metaclass=WithUOWDecorator):
    async def add_user(self, uow: UnitOfWork, user: UserAddSchema):  # noqa
        try:
            password_check = PasswordCheck(password=user.password)
            hashed_password = await password_check.get_hashed_password()
            user_dict = user.model_dump()
            del user_dict["password"]
            user_dict["hashed_password"] = hashed_password
            new_user = await uow.users.add(data=user_dict)
        except IntegrityError as _ex:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=await ErrorResponse(
                    status_code=404,
                    message=f"User with email '{user.email}' or username '{user.username}' is exist",
                ).to_dict_one(),
            )
        return new_user

    async def get_users(self, uow: UnitOfWork):  # noqa
        users = await uow.users.find_all()
        return list(users)

    async def get_user(self, user_id: int, uow: UnitOfWork):  # noqa
        user = await uow.users.get(ident=user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=await ErrorResponse(
                    status_code=404,
                    message="Not Found",
                ).to_dict_one(),
            )
        return user

    async def update_user( # noqa
        self,
        user_id: int,
        uow: UnitOfWork,
        update_user: UserUpdateSchema,
    ):
        values = update_user.model_dump(exclude_unset=True)
        password_check = PasswordCheck(password=values.get("password"))
        hashed_password = await password_check.get_hashed_password()
        del values["password"]
        values["hashed_password"] = hashed_password
        try:
            user = await uow.users.update(user_id=user_id, values=values)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=await ErrorResponse(
                    status_code=400,
                    message=f"User with email '{update_user.email}' or username '{update_user.username}' is exist",
                ).to_dict_one(),
            )
        return user
