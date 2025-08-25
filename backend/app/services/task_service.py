from typing import List
from uuid import UUID

from sqlalchemy import select, func, update
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tasks import Task as TaskModel, TaskStatus
from app.schemas.tasks import CreateTask, UpdateTask, SwapTask
from app.utils.responsive_utils import ResponseUtils

class TaskService:
  @staticmethod
  async def get_task_by_id(db: AsyncSession, task_id: UUID) -> TaskModel:
    query = (select(TaskModel).where(TaskModel.id == task_id))
    result = await db.execute(query)
    task = result.scalar_one_or_none()
    if not task:
      raise NoResultFound(f"Task with ID {task_id} not found")
    return task

  @staticmethod
  async def get_tasks(db: AsyncSession) -> List[TaskModel]:
    query = select(TaskModel)

    result = await db.execute(query)
    tasks = list(result.scalars().all())
    return tasks

  @staticmethod
  async def create_task(db: AsyncSession, task_data: CreateTask) -> TaskModel:
    new_task = TaskModel(
      title=task_data.title,
      description=task_data.description,
      status=TaskStatus.todo,
    )
    db.add(new_task)
    try:
      await db.commit()
      await db.refresh(new_task)
    except IntegrityError:
      await db.rollback()
      raise ResponseUtils.error("Задача с такой позицией уже существует — попробуйте ещё раз")

    return new_task

  @staticmethod
  async def update_task(db: AsyncSession, task_data: UpdateTask) -> TaskModel:
    task = await TaskService.get_task_by_id(db, task_data.id)

    for field, value in task_data.model_dump(exclude_unset=True).items():
      setattr(task, field, value)

    await db.commit()
    await db.refresh(task)

    return task

  @staticmethod
  async def soft_delete_task(db: AsyncSession, task_id: UUID) -> TaskModel:
    return await TaskService._set_hidden(db, task_id, True)

  @staticmethod
  async def restore_task(db: AsyncSession, task_id: UUID) -> TaskModel:
    return await TaskService._set_hidden(db, task_id, False)

  @staticmethod
  async def _set_hidden(db: AsyncSession, task_id: UUID, hidden: bool) -> TaskModel:
    async with db.begin():
      stmt = (
        update(TaskModel)
        .where(TaskModel.id == task_id)
        .values(is_hidden=hidden)
        .returning(TaskModel)
      )
      result = await db.execute(stmt)
      task = result.scalar_one_or_none()
      if not task:
        raise NoResultFound(f"Task with ID {task_id} not found")
    return task

  @staticmethod
  async def delete_task(db: AsyncSession, task_id: UUID) -> None:
    task = await TaskService.get_task_by_id(db, task_id)
    await db.delete(task)
    await db.commit()