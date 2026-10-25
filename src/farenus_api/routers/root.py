import fastapi

from farenus_api import config

router = fastapi.APIRouter()

meta = config.meta


@router.get("/")
def root():
    return {"name": meta["name"], "version": meta["version"]}
