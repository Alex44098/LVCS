from Models.DatabaseConnection import DatabaseConnection
from Models.EventListener import EventListener


class ProjectManagerModel(EventListener):
    def __init__(self):
        super().__init__()

    def get_projects(self):
        connection = DatabaseConnection()
        request = """SELECT * FROM projects;"""
        cursor = connection.get_cursor_query(request)
        cursor.execute(request)
        projects = cursor.fetchall()

        for project in projects:
            yield project

    def open_creator(self):
        self.trigger_event("open_creator")

    def open_project(self):
        self.trigger_event("open_project")
