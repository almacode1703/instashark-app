from fastapi import FastAPI
from contextlib import asynccontextmanager
from util.init_db import create_table

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connected....")
    create_table()
    yield
app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


