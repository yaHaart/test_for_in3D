from pydantic import BaseModel, Field


class Manager(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    surname: str = Field(..., min_length=2, max_length=50)
    job_name: str = Field(..., min_length=3, max_length=50)
    department: str = Field(..., min_length=3, max_length=50)
    birthday: str = Field(..., min_length=10, max_length=10)


class Worker(BaseModel):
    manager_id: int
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    job_name: str = Field(..., min_length=3, max_length=50)
    department: str = Field(..., min_length=3, max_length=50)
    birthday: str = Field(..., min_length=10, max_length=10)

class ManagerDB(Manager):
    id: int


class WorkerDB(Worker):
    id: int