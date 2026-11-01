import contextlib

import fastapi

from farenus_api import config, database
from farenus_api.repositories import weather as weather_repository
from farenus_api.routers import health, root, weather

DEBUG = config.API_DEBUG_MODE


@contextlib.asynccontextmanager
async def lifespan(app):
    database.init_db(weather_repository.SCHEMA)
    yield


app = fastapi.FastAPI(
    lifespan=lifespan,
    title=config.META["name"],
    version=config.META["version"],
    docs_url="/docs" if DEBUG else None,
    redoc_url="/redoc" if DEBUG else None,
    openapi_url="/openapi.json" if DEBUG else None,
)

app.include_router(root.router)
app.include_router(health.router)
app.include_router(weather.router)
