from typing import List

import backend.crud
from backend.model import Worker, WorkerDB
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.post("/", response_model=WorkerDB, status_code=201)
async def create_worker(payload: Worker):
    worker_id = await backend.crud.post_worker(payload)

    response_object = {
        "manager_id": payload.manager_id,
        "id": worker_id,
        "name": payload.name,
        "surname": payload.surname,
        "job_name": payload.job_name,
        "department": payload.department,
        "birthday": payload.birthday,
    }
    return response_object


@router.get("/{id}/", response_model=WorkerDB)
async def read_worker(id: int = Path(..., gt=0), ):
    worker = await backend.crud.get_worker(id)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker


@router.get("/", response_model=List[WorkerDB])
async def read_all_workers():
    return await backend.crud.get_all_workers()


@router.put("/{id}/", response_model=WorkerDB)
async def update_worker(payload: Worker, id: int = Path(..., gt=0), ):
    worker = await backend.crud.get_worker(id)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")

    worker_id = await backend.crud.put_worker(id, payload)

    response_object = {
        "manager_id": payload.manager_id,
        "id": worker_id,
        "name": payload.name,
        "surname": payload.surname,
        "job_name": payload.job_name,
        "department": payload.department,
        "birthday": payload.birthday,
    }
    return response_object


@router.delete("/{id}/", response_model=WorkerDB)
async def delete_worker(id: int = Path(..., gt=0)):
    worker = await backend.crud.get_worker(id)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")

    await backend.crud.delete_worker(id)

    return worker
