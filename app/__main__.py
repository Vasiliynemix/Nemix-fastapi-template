from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from app.api.v1 import routers

app = FastAPI()

for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.__main__:app", reload=True)
