import uuid

from pydantic import BaseModel, EmailStr, ConfigDict


class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr


class UserAddSchema(UserBaseSchema):
    password: str


class UserUpdateSchema(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    hashed_password: str | None = None


class UserShowSchema(UserBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: uuid.UUID
