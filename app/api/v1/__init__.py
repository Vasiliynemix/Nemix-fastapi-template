from .task import router as tasks_router
from app.api.v1.user import router as users_router
from app.api.v1.login import router as login_router

routers = (
    tasks_router,
    users_router,
    login_router,
)
