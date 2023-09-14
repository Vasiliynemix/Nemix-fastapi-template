from app.schemas.tasks import TaskAddSchema
from app.utils.unitofwork import UnitOfWork


class TaskService:
    async def add_task(self, task: TaskAddSchema, uow: UnitOfWork):
        async with uow:
            await uow.tasks.add(data=task)
