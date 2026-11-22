import fastapi

router = fastapi.APIRouter(prefix="/minecraft", tags=["minecraft"])


@router.get("")
def root():
    pass
