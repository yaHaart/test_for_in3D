from fastapi import FastAPI
import asyncio
import create_employee

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "привет"}

@app.get("/admin")
async def root():
    return {"message": 'create_employee.temp_manager.name'}