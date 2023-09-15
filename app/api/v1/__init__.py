from .tasks import router as tasks_router
from app.api.v1.users import router as users_router

routers = (
    tasks_router,
    users_router,
)
