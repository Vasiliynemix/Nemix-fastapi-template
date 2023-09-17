from datetime import timedelta, datetime

from jose import jwt # noqa

from app.config import conf


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
):
    to_encode = data.copy()
    if expires_delta is None:
        expire = datetime.utcnow() + timedelta(minutes=conf.auth.access_token_expire)
    else:
        expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, conf.auth.secret_key, algorithm=conf.auth.token_algorithm)
    return encoded_jwt
