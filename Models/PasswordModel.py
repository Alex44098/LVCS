from Models.EventListener import EventListener
from Models.DatabaseConnection import DatabaseConnection


class PasswordModel(EventListener):
    def __init__(self):
        super().__init__()

    def get_password(self, info_id):
        connection: DatabaseConnection = DatabaseConnection()
        query = f"SELECT password FROM project_info WHERE info_id = {info_id};"
        cursor = connection.get_cursor_query(query)
        return cursor.fetchall()[0][0]
