from uuid import UUID
from sqlalchemy.orm import Session

from app.repositories import TaskRepository
from app.models import Task


class TaskService:
    def __init__(self, db: Session):
        self._repo = TaskRepository(db)

    def list_tasks(self) -> list[Task]:
        return self._repo.get_all()

    def get_task_by_id(self, task_id: UUID) -> Task | None:
        return self._repo.get_by_id(task_id)
