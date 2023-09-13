from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from app.db.models import Base


class Task(Base):
    task_name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]

    creator_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    executor_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
