from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True)
    hashed_password: Mapped[str]
