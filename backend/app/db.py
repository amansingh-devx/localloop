import os

import psycopg
from dotenv import load_dotenv

load_dotenv()  # reads backend/.env into environment variables
DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    """Open a new connection to the LocalLoop PostgreSQL database."""
    return psycopg.connect(DATABASE_URL)