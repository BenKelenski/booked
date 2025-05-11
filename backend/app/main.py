from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.dependencies import create_db_and_tables

from .routers import book_routes, user_routes, collection_routes
from .config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_routes.router, prefix=settings.API_V1_STR)
app.include_router(book_routes.router, prefix=settings.API_V1_STR)
app.include_router(collection_routes.router, prefix=settings.API_V1_STR)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
