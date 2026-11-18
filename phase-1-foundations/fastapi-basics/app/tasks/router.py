from fastapi import APIRouter, status
from .schemas import TaskRead, TaskBase
from .service import task_service
router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
def list_tasks() -> list[TaskRead]:
    tasks: list[TaskRead] = task_service.get_all()
    return tasks


@router.get("/{task_id}")
def get_task_by_id(task_id: int) -> TaskRead:
    task: TaskRead = task_service.get_by_id(task_id)
    return task


@router.post("", status_code=status.HTTP_201_CREATED)
def create_task(data: TaskBase) -> TaskRead:
    task: TaskRead = task_service.create(data)
    return task


@router.patch("/{task_id}/done")
def mark_task_done(task_id: int) -> TaskRead:
    return task_service.mark_done(task_id)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    task_service.delete(task_id)
