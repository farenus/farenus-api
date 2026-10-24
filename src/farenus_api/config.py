import time

import dotenv

env_file = dotenv.dotenv_values(".env")


def _to_bool(value):
    if value is None:
        return False
    return value.strip() in ("True")


API_DEBUG_MODE = _to_bool(env_file.get("API_DEBUG_MODE"))

START_TIME = time.time()
