from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = 'member'
    
class UserUpdate(BaseModel):
    name: str | None=None
    email: EmailStr | None=None
    role: str | None=None
    
class UserOut(BaseModel):
    id: int
    name: str
    email: str
    role: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)