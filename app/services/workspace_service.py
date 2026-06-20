from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models import Workspace
from app.repository.workspace_repository import WorkspaceRepository
from app.schemas.workspace import WorkspaceCreate, WorkspaceUpdate

_repo = WorkspaceRepository()


def create_workspace(db: Session, owner_id: int, data: WorkspaceCreate) -> Workspace:
    return _repo.create(db, owner_id, data)


def get_workspace(db: Session, workspace_id: int, user_id: int) -> Workspace:
    workspace = _repo.get_by_id(db, workspace_id)
    if not workspace:
        raise HTTPException(status_code=404, detail="Workspace não encontrado")
    if workspace.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Acesso negado")
    return workspace


def list_workspaces(db: Session, owner_id: int) -> list[Workspace]:
    return _repo.get_all_by_owner(db, owner_id)


def update_workspace(db: Session, workspace_id: int, user_id: int, data: WorkspaceUpdate) -> Workspace:
    workspace = get_workspace(db, workspace_id, user_id)
    return _repo.update(db, workspace, data)


def delete_workspace(db: Session, workspace_id: int, user_id: int) -> None:
    workspace = get_workspace(db, workspace_id, user_id)
    _repo.delete(db, workspace)
