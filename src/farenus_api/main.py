import contextlib

import fastapi
import fastapi.middleware.cors

from farenus_api import config
from farenus_api import database
from farenus_api import repositories
from farenus_api import routers

DEBUG = config.API_DEBUG_MODE


@contextlib.asynccontextmanager
async def lifespan(app):
    database.init_db(repositories.weather.SCHEMA)
    yield


app = fastapi.FastAPI(
    lifespan=lifespan,
    title=config.META["name"],
    version=config.META["version"],
    docs_url="/docs" if DEBUG else None,
    redoc_url="/redoc" if DEBUG else None,
    openapi_url="/openapi.json" if DEBUG else None,
)

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.root.router)
app.include_router(routers.health.router)
app.include_router(routers.weather.router)
