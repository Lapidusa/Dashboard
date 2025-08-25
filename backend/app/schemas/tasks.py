from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from enum import IntEnum

class TaskStatus(IntEnum):
  todo = 0
  in_progress = 1
  done = 2

class Task(BaseModel):
  title: str
  description: Optional[str]
  class Config:
    from_attributes = True

class CreateTask(Task):
  pass

class UpdateTask(Task):
  id: UUID
  status: TaskStatus

class SwapTask(BaseModel):
  first_task: UUID
  second_task: UUID