import importlib.metadata
import pathlib
import time

import dotenv

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]

ENV_FILE = dotenv.dotenv_values(PROJECT_ROOT / ".env")

META = importlib.metadata.metadata("farenus-api")


def _to_bool(value):
    if value is None:
        return False
    return value.strip() == "True"


API_DEBUG_MODE = _to_bool(ENV_FILE.get("API_DEBUG_MODE"))

START_TIME = time.time()
