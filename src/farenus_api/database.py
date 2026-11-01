import sqlite3

from farenus_api import config


def _sqlite():
    config.SQLITE_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(config.SQLITE_PATH, check_same_thread=False)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.execute("PRAGMA journal_mode = WAL")
    return con


def _open_connection():
    if config.DATABASE_BACKEND == "sqlite":
        return _sqlite()
    raise ValueError(f"nieobsługiwany backend: {config.DATABASE_BACKEND}")


def get_connection():
    con = _open_connection()
    try:
        yield con
    finally:
        con.close()


def init_db(*schemas):
    con = _open_connection()
    try:
        for schema in schemas:
            con.executescript(schema)
    finally:
        con.close()
