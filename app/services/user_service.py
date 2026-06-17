from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models import User
from app.core.security import verify_password, create_access_token
from app.repository.user_repository import UserRepository
from app.schemas.user import UserCreate

def register(db: Session, data: UserCreate) -> User:
    user_repository = UserRepository()
    user = user_repository.get_by_email(db, data.email)
    # verifica email duplicado
    if user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return user_repository.create(db, data)

def login(db: Session, email: str, password: str) -> str:#retorna token:
    user_repository = UserRepository()
    user = user_repository.get_by_email(db, email)
    if not user:
        raise HTTPException(status_code=401, detail='Credenciais inválidas')
    #verifica senha
    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail='Credenciais inválidas')
    #gera token
    return create_access_token({'sub': str(user.id)})
