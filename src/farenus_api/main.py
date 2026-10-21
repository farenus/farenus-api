import importlib.metadata

import fastapi

meta = importlib.metadata.metadata("farenus-api")

app = fastapi.FastAPI(version=meta["version"], title=meta["name"])


@app.get("/")
def root():
    return {"name": meta["name"], "version": meta["version"]}
