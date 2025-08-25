import uuid

from sqlalchemy import Column, Integer, String, Enum, Boolean
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from app.db import Base
from enum import IntEnum

class TaskStatus(IntEnum):
  todo = 0
  in_progress = 1
  done = 2

class Task(Base):
  __tablename__ = "tasks"

  id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  title = Column(String, nullable=False)
  description = Column(String, nullable=True)
  status = Column(Enum(TaskStatus), default=TaskStatus.todo)
  is_hidden=Column(Boolean, nullable=False, default=False)