from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    status: str | None
    priority: int | None
    is_deleted: bool | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TaskListResponse(BaseModel):
    tasks: list[TaskResponse]
