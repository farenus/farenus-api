import datetime

import fastapi
import pydantic

from farenus_api import auth

router = fastapi.APIRouter(prefix="/weather", tags=["weather"])

database = []


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
    "/stations/{station}/measurements",
    status_code=201,
    response_model=MeasurementResponse,
    dependencies=[fastapi.Depends(auth.require_api_key)],
)
def post_measurements(station: str, measurement: MeasurementCreate):
    record = MeasurementResponse(
        id=len(database) + 1,
        station_id=station,
        measured_at=datetime.datetime.now(datetime.UTC),
        **measurement.model_dump(),
    )
    database.append(record)
    return record


@router.get(
    "/stations/{station}/measurements",
    response_model=list[MeasurementResponse],
)
def get_measurements(station: str, limit: int = 100):
    records = [m for m in database if m.station_id == station]
    records.sort(key=lambda m: m.measured_at, reverse=True)
    return records[:limit]
