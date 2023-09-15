from sqlalchemy import select

from app.db.models import User
from app.utils.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model: type[User] = User

    async def get_user_by_username(self, username: str):
        stmt = select(self.model).where(self.model.username == username)
        return await self.session.scalar(stmt)

