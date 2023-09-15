from typing import Annotated, Any

from fastapi import APIRouter, Path, Query, Body
from starlette import status

from app.api.v1.dependencies import UOWDep
from app.api.v1.response import SuccessResponse
from app.schemas.users import UserShowSchema, UserAddSchema, UserUpdateSchema
from app.services.users import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=dict[str, list[UserShowSchema] | Any],
)
async def get_users(
    uow: UOWDep,
    limit: Annotated[int, Query()] = 100,
):
    user = await UserService().get_users(uow=uow)
    response = SuccessResponse(200, user, limit=limit)
    return await response.to_dict_many()


@router.get(
    "/user/{user_id}/",
    status_code=status.HTTP_200_OK,
    response_model=dict[str, UserShowSchema | Any],
)
async def get_user_info(
    uow: UOWDep,
    user_id: Annotated[int, Path()],
):
    user = await UserService().get_user(user_id=user_id, uow=uow)
    response = SuccessResponse(200, user, "Пользователь")
    return await response.to_dict_one()


@router.post(
    "/user/create/",
    status_code=status.HTTP_201_CREATED,
    response_model=dict[str, UserShowSchema | Any],
)
async def create_user(
    uow: UOWDep,
    user: Annotated[UserAddSchema, Body()],
):
    user = await UserService().add_user(uow=uow, user=user)
    response = SuccessResponse(201, user, "User create!")
    return await response.to_dict_one()


@router.put(
    "/user/{user_id}/update/",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=dict[str, UserShowSchema | Any],
)
async def update_user(
    uow: UOWDep,
    user_id: Annotated[int, Path()],
    update_user_data: Annotated[UserUpdateSchema, Body()],
):
    user = await UserService().update_user(
        uow=uow,
        user_id=user_id,
        update_user=update_user_data,
    )
    response = SuccessResponse(202, user, "User update!")
    return await response.to_dict_one()
