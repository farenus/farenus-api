# farenus-api

api backend for farenus network.

## Uruchomienie lokalne

```bash
git clone https://github.com/farenus/farenus-api.git
uv sync
uv run uvicorn farenus_api.main:app --reload
```

API działa pod `http://127.0.0.1:8000`, a dokumentacja (Swagger UI) pod `/docs`.
