from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/users', tags=["Users"])


@router.get("/")
async def root():
    return {"Hello": "world!"}
