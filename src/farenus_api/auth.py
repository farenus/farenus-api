import pydantic

from farenus_api import config

API_KEY_PREFIX = "API_KEY_HASH_"


class Caller(pydantic.BaseModel):
    name: str


def _load_api_keys() -> dict[str, Caller]:
    api_keys: dict[str, Caller] = {}
    for var_name, value in config.env_file.items():
        if not var_name.startswith(API_KEY_PREFIX):
            continue
        if not value:
            raise ValueError(f"brak klucza w {var_name}")
        name = var_name.removeprefix(API_KEY_PREFIX).lower()
        api_keys[value] = Caller(name=name)
    return api_keys
