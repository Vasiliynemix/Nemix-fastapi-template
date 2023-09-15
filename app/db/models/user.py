import uuid

from sqlalchemy import LargeBinary
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary)
    email: Mapped[str] = mapped_column(unique=True)
