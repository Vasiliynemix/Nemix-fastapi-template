import uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models import Base


class User(Base):
    user_id: Mapped[uuid.UUID] = mapped_column(unique=True, default=uuid.uuid4(), primary_key=True)

    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True)
