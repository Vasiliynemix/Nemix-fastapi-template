import logging

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from starlette import status

from app.logger import logger
from app.schemas.users import UserAddSchema
from app.utils.decorators import WithUOWDecorator
from app.utils.unitofwork import UnitOfWork


class UserService(metaclass=WithUOWDecorator):
    async def add_user(self, uow: UnitOfWork, user: UserAddSchema): # noqa
        try:
            user_dict = user.model_dump()
            user = await uow.users.add(data=user_dict)
        except IntegrityError as _ex:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Такой пользователь уже существует',
            )
        return user

    async def get_users(self, uow: UnitOfWork): # noqa
        users = await uow.users.find_all()
        return list(users)

    async def get_user(self, user_id: int, uow: UnitOfWork): # noqa
        user = await uow.users.get(ident=user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Not Found',
            )
        return user
