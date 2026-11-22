import fastapi

from farenus_api import config

router = fastapi.APIRouter(tags=["root"])


@router.get("/")
def root():
    return {
        "name": config.META["name"],
        "version": config.META["version"],
        "source": "https://github.com/farenus/farenus-api",
    }
