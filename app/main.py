import uvicorn
from fastapi import FastAPI
from api import routers

app = FastAPI()
for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
