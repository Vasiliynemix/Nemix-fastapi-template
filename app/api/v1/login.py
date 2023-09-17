from typing import Annotated, Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.v1.dependencies.auth_token import (
    get_current_username_from_token,
)
from app.api.v1.dependencies.uow import UOWDep
from app.api.v1.response import SuccessResponse
from app.schemas.login import Token
from app.schemas.users import UserShowSchema
from app.services.login import LoginService

router = APIRouter(prefix="/login", tags=["Auth"])


@router.post("/token", response_model=Token)
async def login_with_access_token(
    uow: UOWDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    user = await LoginService().authenticate_user(
        uow=uow,
        password=form_data.password,
        username=form_data.username,
    )
    token = await LoginService().create_token_for_username(user=user)
    return token


@router.get("/test_auth_endpoint", response_model=dict[str, UserShowSchema | Any])
async def sample_endpoint_under_jwt(
    uow: UOWDep,
    username: Annotated[str, Depends(get_current_username_from_token)],
):
    user = await LoginService().get_user_by_username_in_depends(uow=uow, username=username)
    response = SuccessResponse(202, user)
    return await response.to_dict_one()
