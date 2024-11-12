from Models.DatabaseConnection import DatabaseConnection
from Models.EventListener import EventListener
from Models.Project import Project


class ProjectManagerModel(EventListener):
    def __init__(self):
        super().__init__()

    def get_projects(self):
        connection = DatabaseConnection()
        request = "SELECT * FROM projects;"
        cursor = connection.get_cursor_query(request)
        cursor.execute(request)
        projects_db = cursor.fetchall()
        projects = []
        for project_db in projects_db:
            project = Project(project_db[0], project_db[1], project_db[2], project_db[3])
            projects.append(project)
        return projects

    def open_creator(self):
        self.trigger_event("open_creator")

    def open_project(self):
        self.trigger_event("open_project")
