import sqlite3

DATABASE_PATH = 'db/database.db'

def get_connection():
    """Obtiene una conexión a la base de datos."""
    return sqlite3.connect(DATABASE_PATH)