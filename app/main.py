from fastapi import FastAPI

from app.db.base import Base
from app.db import models
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Task B2B',
    description='Task Manager B2B',
    version='1.0.0'
)

@app.get('/health')
async def health():
    return {'status': 'OK'}
