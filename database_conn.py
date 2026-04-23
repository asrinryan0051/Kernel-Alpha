import sqlite3
import os

#DATABASE CONNECTION
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "projectx.db")

def get_db_connection():
    # Opening in Read-Only mode
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn