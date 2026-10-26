import time

import fastapi

from farenus_api import auth, config

router = fastapi.APIRouter(prefix="/health", tags=["health"])


@router.get("/", dependencies=[fastapi.Depends(auth.require_api_key)])
def get_health():
    return {"status": "ok", "uptime_seconds": round(time.time() - config.START_TIME)}
