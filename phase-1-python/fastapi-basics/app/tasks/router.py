from fastapi import APIRouter, HTTPException
from .schemas import TaskRead, TaskAdd
from .service import task_service
router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
def list_tasks() -> list[TaskRead]:
    # Since we operate on mock data there is no need to handle error like we do in get by id method.
    tasks: list[TaskRead] = task_service.get_all()
    return tasks


@router.get("/{task_id}")
def get_task_by_id(task_id: int) -> TaskRead:
    task: TaskRead | None = task_service.get_by_id(task_id)
    if task == None:
        raise HTTPException(
            status_code=404, detail=f"Task {task_id} not found")
    else:
        return task


@router.post("")
def create_task(data: TaskAdd) -> TaskRead:
    task: TaskRead = task_service.create(data)
    return task


@router.delete("/{task_id}")
def delete_task(task_id: int) -> None:
    task_service.delete(task_id)
