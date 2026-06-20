from sqlalchemy.orm import Session

from app.db.models import Workspace
from app.schemas.workspace import WorkspaceCreate, WorkspaceUpdate


class WorkspaceRepository:
    def create(self, db: Session, owner_id: int, data: WorkspaceCreate) -> Workspace:
        workspace = Workspace(name=data.name, owner_id=owner_id)
        db.add(workspace)
        db.commit()
        db.refresh(workspace)
        return workspace

    def get_by_id(self, db: Session, workspace_id: int) -> Workspace | None:
        return db.query(Workspace).filter(Workspace.id == workspace_id).first()

    def get_all_by_owner(self, db: Session, owner_id: int) -> list[Workspace]:
        return db.query(Workspace).filter(Workspace.owner_id == owner_id).all()

    def update(self, db: Session, workspace: Workspace, data: WorkspaceUpdate) -> Workspace:
        if data.name is not None:
            workspace.name = data.name
        db.commit()
        db.refresh(workspace)
        return workspace

    def delete(self, db: Session, workspace: Workspace) -> None:
        db.delete(workspace)
        db.commit()
