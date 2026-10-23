import importlib.metadata
import time

import fastapi

from farenus_api import auth, config

DEBUG = config.API_DEBUG_MODE

meta = importlib.metadata.metadata("farenus-api")

app = fastapi.FastAPI(
    title=meta["name"],
    version=meta["version"],
    docs_url="/docs" if DEBUG else None,
    redoc_url="/redoc" if DEBUG else None,
    openapi_url="/openapi.json" if DEBUG else None,
)


@app.get("/")
def root():
    return {"name": meta["name"], "version": meta["version"]}


@app.get("/health", dependencies=[fastapi.Depends(auth.require_api_key)])
def get_health():
    return {"status": "ok", "uptime_seconds": round(time.time() - config.START_TIME)}
