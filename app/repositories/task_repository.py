from uuid import UUID
from sqlalchemy.orm import Session
from app.models import Task


class TaskRepository:
    def __init__(self, db: Session):
        self._db = db

    def get_all(self, *, exclude_deleted: bool = True) -> list[Task]:
        q = self._db.query(Task)
        if exclude_deleted:
            q = q.filter(Task.is_deleted != True)
        return q.order_by(Task.created_at.desc()).all()

    def get_by_id(self, task_id: UUID, *, exclude_deleted: bool = True) -> Task | None:
        q = self._db.query(Task).filter(Task.id == task_id)
        if exclude_deleted:
            q = q.filter(Task.is_deleted != True)
        return q.first()
