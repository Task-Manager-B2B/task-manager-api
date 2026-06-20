from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    workspace_id: int


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class ProjectOut(BaseModel):
    id: int
    name: str
    description: str | None
    workspace_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
