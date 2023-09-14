from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from starlette import status

from app.schemas.users import UserAddSchema
from app.utils.unitofwork import UnitOfWork


class UserService:
    @staticmethod
    async def add_user(user: UserAddSchema, uow: UnitOfWork):
        async with uow:
            try:
                user_dict = user.model_dump()
                user = await uow.users.add(data=user_dict)
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Такой пользователь уже существует',
                )
        return user

    @staticmethod
    async def get_users(uow: UnitOfWork):
        async with uow:
            users = await uow.users.find_all()
        return list(users)

    @staticmethod
    async def get_user(user_id: int, uow: UnitOfWork):
        async with uow:
            user = await uow.users.get(ident=user_id)
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Not Found',
                )
        return user
