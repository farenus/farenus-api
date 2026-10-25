import importlib.metadata
import pathlib
import time

import dotenv

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]

env_file = dotenv.dotenv_values(PROJECT_ROOT / ".env")

meta = importlib.metadata.metadata("farenus-api")


def _to_bool(value):
    if value is None:
        return False
    return value.strip() == "True"


API_DEBUG_MODE = _to_bool(env_file.get("API_DEBUG_MODE"))

START_TIME = time.time()
