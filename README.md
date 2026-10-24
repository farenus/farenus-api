# farenus-api

api backend for farenus network.

## Konfiguracja

Konfiguracja jest wczytywana ze zmiennych środowiskowych zapisanych w pliku `.env` (patrz `config.py`)

## Klucze API

Skrypt generujący klucz uwierzytelniający oraz jego hash:

```bash
uv run python scripts/keygen.py
```

## Uruchomienie lokalne

```bash
git clone https://github.com/farenus/farenus-api.git
uv sync
uv run uvicorn farenus_api.main:app --reload
```

API działa pod `http://127.0.0.1:8000`, a dokumentacja (Swagger UI) pod `/docs`.

## Wdrożenie na serwer

Pierwsze wdrożenie:

```bash
curl -LsSf https://astral.sh/uv/install.sh | UV_UNMANAGED_INSTALL=/usr/local/bin sh
export PATH="/usr/local/bin:$PATH"
echo 'export PATH="/usr/local/bin:$PATH"' >> /root/.bashrc
export UV_PYTHON_INSTALL_DIR=/opt/uv-python
echo 'export UV_PYTHON_INSTALL_DIR=/opt/uv-python' >> /root/.bashrc

useradd --system --no-create-home --shell /usr/sbin/nologin api
install -d -o api -g api -m 750 /var/lib/api

git clone https://github.com/farenus/farenus-api.git /opt/api
cd /opt/api
git checkout vX.Y.Z

uv sync --locked --no-dev

cp .env.example .env
chown root:api .env
chmod 640 .env

cp deploy/farenus-api.service /etc/systemd/system/   # patrz niżej
systemctl daemon-reload
systemctl enable --now farenus-api
```

**Przed wdrożeniem zmień `PROXY_IP`** w `--forwarded-allow-ips=PROXY_IP` na adres IP serwera proxy.

Aktualizacja do nowej wersji:

```bash
cd /opt/api
git fetch --tags
git checkout vX.Y.Z

uv sync --locked --no-dev

systemctl restart farenus-api
```

Jeśli zmienił się plik `deploy/farenus-api.service`, skopiuj go ponownie i wykonaj `systemctl daemon-reload`.

## Obsługa na serwerze

```bash
systemctl status farenus-api   # stan usługi
journalctl -u farenus-api -f   # logi na żywo

systemctl restart farenus-api  # restart
systemctl stop farenus-api     # zatrzymanie
systemctl start farenus-api    # uruchomienie
```
