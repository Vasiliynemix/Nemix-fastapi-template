import uvicorn
from fastapi import FastAPI
from api.v1 import routers

app = FastAPI()
for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
