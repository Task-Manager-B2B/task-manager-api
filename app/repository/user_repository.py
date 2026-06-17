from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password

class UserRepository:
    def create(self, db: Session, data: UserCreate) -> User:
        hashed = hash_password(data.password)
        user = User(**data.model_dump(exclude={'password'}), password=hashed)
        
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user

    def get_by_id(self, db: Session, user_id: int) -> User | None:
        return db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    def update(self, db: Session, user: User, data: UserUpdate) -> User:
        if data.name is not None:
            user.name = data.name
        if data.email is not None:
            user.email = data.email
        if data.role is not None:
            user.role = data.role
        db.commit()
        db.refresh(user)
        return user

    def delete(self, db: Session, user: User) -> None:
        db.delete(user)
        db.commit()
    