from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)


class TaskRead(TaskBase):
    id: int
    done: bool = False
