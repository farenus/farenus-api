import datetime

SCHEMA = """
CREATE TABLE IF NOT EXISTS measurements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    station_id TEXT NOT NULL,
    measured_at TEXT NOT NULL,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    pressure REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_measurements_station_time
    ON measurements (station_id, measured_at DESC);
"""


def insert_measurement(con, station_id, temperature, humidity, pressure):
    measured_at = datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds")
    with con:
        cursor = con.execute(
            "INSERT INTO measurements "
            "(station_id, measured_at, temperature, humidity, pressure) "
            "VALUES (?, ?, ?, ?, ?)",
            (station_id, measured_at, temperature, humidity, pressure),
        )
    return {
        "id": cursor.lastrowid,
        "station_id": station_id,
        "measured_at": measured_at,
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure,
    }


def list_measurements(con, station_id, limit):
    rows = con.execute(
        "SELECT * FROM measurements WHERE station_id = ? "
        "ORDER BY measured_at DESC LIMIT ?",
        (station_id, limit),
    ).fetchall()
    return [dict(row) for row in rows]
