from fastapi import APIRouter
from app.routers.task import router as task_router
main_router = APIRouter()

main_router.include_router(task_router, prefix="/task", tags=["Task"])