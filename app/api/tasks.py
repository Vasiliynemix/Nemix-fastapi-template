from fastapi import APIRouter

from app.api.dependencies import UOWDep
from app.services.tasks import TaskService

router = APIRouter(prefix='/api/v1/tasks', tags=["Tasks"])

