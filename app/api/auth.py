from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services import user_service
from app.schemas.user import UserCreate, UserLogin

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post('/register')
def register(data: UserCreate, db: Session = Depends(get_db)):
    return user_service.register(db, data)

@router.post('/login')
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = user_service.login(db, data.email, data.password)
    return {"access_token": token, "token_type": "bearer"}
    
@router.post('/logout')
def logout():
    return {'message': 'Logout realizado com sucesso'}