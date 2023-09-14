from app.db.models import Task
from app.utils.repository import SQLAlchemyRepository


class TasksRepository(SQLAlchemyRepository):
    model: type[Task] = Task
