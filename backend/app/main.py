from fastapi import FastAPI

from app.db import get_connection

app = FastAPI(title="LocalLoop API")


@app.get("/")
def root():
    return {"message": "LocalLoop API is running"}


@app.get("/api/health")
def health():
    """Checks that the API can reach PostgreSQL and PostGIS."""
    with get_connection() as conn:
        db_version = conn.execute("SELECT version()").fetchone()[0]
        postgis = conn.execute("SELECT postgis_version()").fetchone()[0]
    return {"status": "ok", "database": db_version, "postgis": postgis}