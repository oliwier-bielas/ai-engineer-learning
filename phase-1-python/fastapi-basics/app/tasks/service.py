from .schemas import TaskRead, TaskAdd


class TaskService:
    tasks: list[TaskRead] = []
    id_increment_number: int = 5

    def __init__(self) -> None:
        self.tasks = [
            TaskRead(id=1, title="Buy milk", done=True),
            TaskRead(id=2, title="Go to barber", done=False),
            TaskRead(id=3, title="Learn FastAPI :)", done=False),
            TaskRead(id=4, title="Take out the rubbish", done=False),
        ]

    def get_all(self) -> list[TaskRead]:
        return self.tasks

    def get_by_id(self, task_id: int) -> TaskRead | None:
        task: TaskRead | None = next(
            (task for task in self.tasks if task.id == task_id), None)
        return task

    def create(self, data: TaskAdd) -> TaskRead:
        task = TaskRead(id=self.id_increment_number,
                        title=data.title, done=data.done)
        self.tasks.append(task)
        self.id_increment_number += 1
        return task

    def delete(self, task_id: int) -> None:
        task: TaskRead | None = self.get_by_id(task_id)
        self.tasks.remove(task)


task_service = TaskService()
