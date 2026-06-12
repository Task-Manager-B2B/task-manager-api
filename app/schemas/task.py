from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

# o que o cliente manda pra criar
class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: str = "todo"
    project_id: int

# o que o cliente manda pra atualizar (tudo opcional)
class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None

# o que a API devolve
class TaskOut(BaseModel):
    id: int
    title: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)