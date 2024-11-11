from Utils.Singleton import singleton
import sqlite3


@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def get_cursor_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor
