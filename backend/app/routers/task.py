from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.schemas.tasks import SwapTask, CreateTask, UpdateTask
from app.services.task_service import TaskService
from app.utils.responsive_utils import ResponseUtils
from app.services.websocket_manager import manager
router = APIRouter()

@router.get("/")
async def get_tasks_endpoint(db: AsyncSession = Depends(get_db)):
  tasks = await TaskService.get_tasks(db)
  return ResponseUtils.success(tasks=tasks)

@router.get("/{task_id}")
async def get_task_endpoint(task_id: UUID, db: AsyncSession = Depends(get_db)):
  task = await TaskService.get_task_by_id(db, task_id)
  return ResponseUtils.success(task=task)

@router.post('/create-task/')
async def create_task_endpoint(task_data: CreateTask,db: AsyncSession = Depends(get_db)):
  if task_data.title is None:
    return ResponseUtils.error("Заголовок обязательный")
  new_task = await TaskService.create_task(db, task_data)
  await manager.broadcast("tasks_updated")
  return ResponseUtils.success(task=new_task)

@router.put("/{task_id}")
async def update_task_endpoint(task_data: UpdateTask, db: AsyncSession = Depends(get_db)):
  updated_task = await TaskService.update_task(db, task_data)
  await manager.broadcast("tasks_updated")
  return ResponseUtils.success(task=updated_task)

@router.delete("/soft-delete-task/{task_id}")
async def soft_delete_task_endpoint(task_id: UUID, db: AsyncSession = Depends(get_db)):
  try:
    await TaskService.soft_delete_task(db, task_id)
    await manager.broadcast("tasks_updated")
    return ResponseUtils.success(message="Задача мягко удалена")
  except NoResultFound:
    return ResponseUtils.error(message="Задача не найдена")

@router.patch("/restore-task/{task_id}")
async def restore_task_endpoint(task_id: UUID, db: AsyncSession = Depends(get_db)):
  try:
    await TaskService.restore_task(db, task_id)
    return ResponseUtils.success(message="Задача восстановлена")
  except NoResultFound:
    return ResponseUtils.error(message="Задача не найдена")

@router.delete("/{task_id}")
async def delete_task_endpoint(task_id: UUID, db: AsyncSession = Depends(get_db)):
  try:
    await TaskService.delete_task(db, task_id)
    await manager.broadcast("tasks_updated")
    return ResponseUtils.success(message="Задача удалена")
  except NoResultFound:
    return ResponseUtils.error(message="Задача не найдена")