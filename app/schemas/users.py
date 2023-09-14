import uuid

from pydantic import BaseModel, EmailStr, ConfigDict


class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr


class UserAddSchema(UserBaseSchema):
    hashed_password: str


class UserShowSchema(UserBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    user_id: uuid.UUID
