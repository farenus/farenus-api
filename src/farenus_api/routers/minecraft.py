import fastapi
import pydantic

from farenus_api import auth
from farenus_api import services

router = fastapi.APIRouter(prefix="/minecraft", tags=["minecraft"])


class WhitelistCreate(pydantic.BaseModel):
    player: str = pydantic.Field(pattern=r"^[A-Za-z0-9_]{3,16}$")


class WhitelistResponse(pydantic.BaseModel):
    player: str


@router.get("")
def root():
    pass


@router.post(
    "/whitelist/add",
    status_code=201,
    response_model=WhitelistResponse,
    dependencies=[fastapi.Depends(auth.require_api_key)],
)
async def whitelist_add(data: WhitelistCreate):
    return await services.minecraft.whitelist_add(data.player)


@router.post(
    "/whitelist/remove",
    status_code=201,
    response_model=WhitelistResponse,
    dependencies=[fastapi.Depends(auth.require_api_key)],
)
async def whitelist_remove(data: WhitelistCreate):
    return await services.minecraft.whitelist_remove(data.player)
