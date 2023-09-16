from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(length=1024))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)
