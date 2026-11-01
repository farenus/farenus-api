import datetime
import typing

import fastapi
import pydantic

from farenus_api import auth, database
from farenus_api.repositories import weather as weather_repository

router = fastapi.APIRouter(prefix="/weather", tags=["weather"])

connection = typing.Annotated[typing.Any, fastapi.Depends(database.get_connection)]


class MeasurementCreate(pydantic.BaseModel):
    temperature: float
    humidity: float
    pressure: float


class MeasurementResponse(MeasurementCreate):
    station_id: str
    id: int
    measured_at: datetime.datetime


@router.get("")
def root():
    pass


@router.post(
    "/stations/{station_id}/measurements",
    status_code=201,
    response_model=MeasurementResponse,
    dependencies=[fastapi.Depends(auth.require_api_key)],
)
def post_measurements(
    station_id: str,
    measurement: MeasurementCreate,
    con: connection,
):
    return weather_repository.insert_measurement(
        con, station_id, **measurement.model_dump()
    )


@router.get(
    "/stations/{station_id}/measurements",
    response_model=list[MeasurementResponse],
)
def get_measurements(
    station_id: str,
    con: connection,
    limit: int = 60,
):
    return weather_repository.list_measurements(con, station_id, limit)
