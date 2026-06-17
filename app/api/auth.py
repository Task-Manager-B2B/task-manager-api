from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post('/register')
def register():
    pass

@router.post('/login')
def login():
    pass

@router.post('/logout')
def logout():
    pass