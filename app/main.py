from fastapi import FastAPI
from app.routers import index_router # Import 'index_router' file from 'app.routers'

app = FastAPI()

app.include_router(index_router.router, prefix="")


