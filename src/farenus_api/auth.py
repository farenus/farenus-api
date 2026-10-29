import hashlib
import typing

import fastapi
import fastapi.security
import pydantic

from farenus_api import config

_API_KEY_PREFIX = "API_KEY_HASH_"


class Caller(pydantic.BaseModel):
    name: str


def _load_api_keys() -> dict[str, Caller]:
    api_keys: dict[str, Caller] = {}
    for var_name, value in config.ENV_FILE.items():
        if not var_name.startswith(_API_KEY_PREFIX):
            continue
        if not value:
            raise ValueError(f"brak klucza w {var_name}")
        name = var_name.removeprefix(_API_KEY_PREFIX).lower()
        api_keys[value] = Caller(name=name)
    return api_keys


def _hash_key(raw_key: str) -> str:
    return hashlib.sha256(raw_key.encode()).hexdigest()


_API_KEYS = _load_api_keys()
_api_key_header = fastapi.security.APIKeyHeader(name="X-API-Key")


def require_api_key(
    api_key: typing.Annotated[str, fastapi.Depends(_api_key_header)],
) -> Caller:
    caller = _API_KEYS.get(_hash_key(api_key))
    if caller is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "X-API-Key"},
        )
    return caller
