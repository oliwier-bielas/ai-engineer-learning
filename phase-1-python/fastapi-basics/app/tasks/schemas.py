from pydantic import BaseModel


class TaskRead(BaseModel):
    id: int
    title: str
    done: bool

class TaskAdd(BaseModel):
    title:str
    done: bool = False