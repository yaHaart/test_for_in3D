import backend.managers
import backend.ping
from backend.db import database, engine, metadata
from fastapi import FastAPI

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(backend.ping.router)
app.include_router(backend.managers.router, prefix="/managers", tags=["managers"])
