from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models import User
from app.core.dependencies import get_current_user
from app.services import workspace_service
from app.schemas.workspace import WorkspaceCreate, WorkspaceUpdate, WorkspaceOut

router = APIRouter(prefix="/workspaces", tags=["Workspaces"])


@router.post("/", response_model=WorkspaceOut, status_code=status.HTTP_201_CREATED)
def create(data: WorkspaceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workspace_service.create_workspace(db, current_user.id, data)


@router.get("/", response_model=list[WorkspaceOut])
def list_all(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workspace_service.list_workspaces(db, current_user.id)


@router.get("/{workspace_id}", response_model=WorkspaceOut)
def get(workspace_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workspace_service.get_workspace(db, workspace_id, current_user.id)


@router.patch("/{workspace_id}", response_model=WorkspaceOut)
def update(workspace_id: int, data: WorkspaceUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return workspace_service.update_workspace(db, workspace_id, current_user.id, data)


@router.delete("/{workspace_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(workspace_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    workspace_service.delete_workspace(db, workspace_id, current_user.id)
