from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password

# - create(db, data: UserCreate) -> User
# - get_by_id(db, user_id: int) -> User | None
# - get_by_email(db, email: str) -> User | None — essencial pro login
# - update(db, user: User, data: UserUpdate) -> User
# - delete(db, user: User) -> None