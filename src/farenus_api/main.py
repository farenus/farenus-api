import importlib.metadata

import fastapi

meta = importlib.metadata.metadata("farenus-api")

api = fastapi.FastAPI(version=meta["version"], title=meta["name"])


@api.get("/")
def root():
    return {"name": meta["name"], "version": meta["version"]}
