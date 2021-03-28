from typing import List

import backend.crud
from backend.model import Manager, ManagerDB
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.post("/", response_model=ManagerDB, status_code=201)
async def create_note(payload: Manager):
    manager_id = await backend.crud.post(payload)

    response_object = {
        "id": manager_id,
        "name": payload.name,
        "surname": payload.surname,
        "job_name": payload.job_name,
        "department": payload.department,
        "birthday": payload.birthday,
    }
    return response_object


@router.get("/{id}/", response_model=ManagerDB)
async def read_manager(id: int = Path(..., gt=0), ):
    manager = await backend.crud.get(id)
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")
    return manager


@router.get("/", response_model=List[ManagerDB])
async def read_all_managers():
    return await backend.crud.get_all()


@router.put("/{id}/", response_model=ManagerDB)
async def update_note(payload: Manager, id: int = Path(..., gt=0),):
    manager = await backend.crud.get(id)
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")

    manager_id = await backend.crud.put(id, payload)

    response_object = {
        "id": manager_id,
        "name": payload.name,
        "surname": payload.surname,
        "job_name": payload.job_name,
        "department": payload.department,
        "birthday": payload.birthday,
    }
    return response_object


@router.delete("/{id}/", response_model=ManagerDB)
async def delete_manager(id: int = Path(..., gt=0)):
    manager = await backend.crud.get(id)
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")

    await backend.crud.delete(id)

    return manager
