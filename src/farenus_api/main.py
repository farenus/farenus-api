import fastapi

from farenus_api import config
from farenus_api.routers import health, root

DEBUG = config.API_DEBUG_MODE

meta = config.meta

app = fastapi.FastAPI(
    title=meta["name"],
    version=meta["version"],
    docs_url="/docs" if DEBUG else None,
    redoc_url="/redoc" if DEBUG else None,
    openapi_url="/openapi.json" if DEBUG else None,
)

app.include_router(root.router)
app.include_router(health.router)
