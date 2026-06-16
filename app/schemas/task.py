from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: str = "todo"
    priority: str = "medium"
    project_id: int
    assignee_id: int | None = None
    due_date: datetime | None = None

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    assignee_id: int | None = None
    due_date: datetime | None = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str
    priority: str
    project_id: int
    assignee_id: int | None = None
    due_date: datetime | None = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)