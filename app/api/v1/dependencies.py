from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status

from app.api.v1.response import ErrorResponse
from app.config import conf
from app.utils.unitofwork import UnitOfWork, IUnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/login/token")


async def get_current_username_from_token(
    token: str = Depends(oauth2_schema),
) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=await ErrorResponse(
            status_code=401,
            message=f"Could not validate credentials",
        ).to_dict_one(),
    )
    try:
        payload = jwt.decode(
            token,
            conf.auth.secret_key,
            algorithms=[conf.auth.token_algorithm]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username
