import uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models import Base


class User(Base):
    user_id: Mapped[uuid.UUID] = mapped_column(unique=True, default=uuid.uuid4(), primary_key=True)

    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
