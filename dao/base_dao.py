from config.config import get_connection

class BaseDAO:
    def __init__(self):
        self.connection = get_connection()

    def execute(self, query, params=()):
        """Ejecuta una consulta SQL."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor