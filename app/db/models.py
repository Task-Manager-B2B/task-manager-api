from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), index=True, unique=True)
    password: Mapped[str]
    role: Mapped[str] = mapped_column(String(20), default='member')
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    memberships: Mapped[list['WorkspaceMember']] = relationship('WorkspaceMember', back_populates='user')
    tasks: Mapped[list['Task']] = relationship('Task', back_populates='assignee')
    
class Workspace(Base):
    __tablename__ = 'workspaces'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    members: Mapped[list["WorkspaceMember"]] = relationship(back_populates="workspace")
    projects: Mapped[list["Project"]] = relationship(back_populates="workspace")
    
class WorkspaceMember(Base):
    __tablename__ = 'workspace_members'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    workspace_id: Mapped[int] = mapped_column(ForeignKey('workspaces.id'))
    role: Mapped[str] = mapped_column(String(20))  # admin | member | viewer
    joined_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    user: Mapped["User"] = relationship(back_populates="memberships")
    workspace: Mapped["Workspace"] = relationship(back_populates="members")

    
class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    workspace_id: Mapped[int] = mapped_column(ForeignKey('workspaces.id'))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    workspace: Mapped["Workspace"] = relationship(back_populates="projects")
    tasks: Mapped[list["Task"]] = relationship(back_populates="project")
    
class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'))
    assignee_id: Mapped[Optional[int]] = mapped_column(ForeignKey('users.id'), nullable=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default='todo')      # todo | in_progress | review | done
    priority: Mapped[str] = mapped_column(String(20), default='medium')  # low | medium | high | urgent
    due_date: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    project: Mapped["Project"] = relationship(back_populates="tasks")
    assignee: Mapped[Optional["User"]] = relationship(back_populates="tasks")    
    