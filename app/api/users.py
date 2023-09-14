from typing import Annotated

from fastapi import APIRouter, Path
from starlette import status

from app.api.dependencies import UOWDep
from app.schemas.users import UserAddSchema, UserShowSchema
from app.services.users import UserService

router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserShowSchema,
)
async def add_user(
    user: UserAddSchema,
    uow: UOWDep,
):
    return await UserService().add_user(uow=uow, user=user)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[UserShowSchema],
)
async def get_users(
    uow: UOWDep,
):
    return await UserService().get_users(uow=uow)


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserShowSchema,
)
async def get_user(user_id: Annotated[int, Path()], uow: UOWDep):
    return await UserService().get_user(user_id=user_id, uow=uow)
