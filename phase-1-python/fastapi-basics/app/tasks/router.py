from fastapi import APIRouter
from .schemas import TaskRead

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
def list_tasks() -> list[TaskRead]:
    return [
        {"id": 1, "title": "Buy milk", "done": False},
        {"id": 2, "title": "Learn FastAPI", "done": True}
    ]
