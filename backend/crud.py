from backend.model import Manager
from backend.model import Worker
from backend.db import managers, workers, database


async def post(payload: Manager):
    query = managers.insert().values(id=payload.id, name=payload.name, surname=payload.surname, job_name=payload.job_name,
                                     department=payload.department, birthday=payload.birthday)
    return await database.execute(query=query)


async def get(id: int):
    query = managers.select().where(id == managers.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = managers.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: Manager):
    query = (
        managers
        .update()
        .where(id == managers.c.id)
        .values(name=payload.name, surname=payload.surname, job_name=payload.job_name, department=payload.department,
                birthday=payload.birthday)
        .returning(managers.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = managers.delete().where(id == managers.c.id)
    return await database.execute(query=query)


async def post_worker(payload: Worker):
    query = workers.insert().values(manager_id=payload.manager_id, id=payload.id, name=payload.name, surname=payload.surname,
                                    job_name=payload.job_name, department=payload.department, birthday=payload.birthday)
    return await database.execute(query=query)


async def get_worker(id: int):
    query = workers.select().where(id == workers.c.id)
    return await database.fetch_one(query=query)


async def get_all_workers():
    query = workers.select()
    return await database.fetch_all(query=query)


async def put_worker(id: int, payload: Worker):
    query = (
        workers
        .update()
        .where(id == workers.c.id)
        .values(manager_id=payload.manager_id, name=payload.name, surname=payload.surname, job_name=payload.job_name, department=payload.department,
                birthday=payload.birthday)
        .returning(workers.c.id)
    )
    return await database.execute(query=query)


async def delete_worker(id: int):
    query = workers.delete().where(id == workers.c.id)
    return await database.execute(query=query)
