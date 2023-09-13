from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped


class Base(DeclarativeBase):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __allow_unmapped__ = False

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, unique=True)

    create_at: Mapped[datetime] = mapped_column(default=func.now())
    update_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())
