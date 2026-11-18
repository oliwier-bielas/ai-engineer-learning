from .schemas import TaskRead, TaskBase
from fastapi import HTTPException


class TaskService:

    def __init__(self) -> None:
        self._id_increment_number: int = 5
        self._tasks: list[TaskRead] = [
            TaskRead(id=1, title="Buy milk", done=True),
            TaskRead(id=2, title="Go to barber", done=False),
            TaskRead(id=3, title="Learn FastAPI :)", done=False),
            TaskRead(id=4, title="Take out the rubbish", done=False),
        ]

    def get_all(self) -> list[TaskRead]:
        return self._tasks

    def get_by_id(self, task_id: int) -> TaskRead:
        task: TaskRead | None = next(
            (task for task in self._tasks if task.id == task_id), None)
        if task is None:
            raise HTTPException(
                status_code=404, detail=f"Task {task_id} not found")

        return task

    def create(self, data: TaskBase) -> TaskRead:
        task = TaskRead(id=self._id_increment_number,
                        title=data.title)
        self._tasks.append(task)
        self._id_increment_number += 1
        return task

    def mark_done(self, task_id: int) -> TaskRead:
        task: TaskRead = self.get_by_id(task_id)
        task.done = True
        return task

    def delete(self, task_id: int) -> None:
        task: TaskRead = self.get_by_id(task_id)
        self._tasks.remove(task)


task_service = TaskService()
