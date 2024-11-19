from Models.DatabaseConnection import DatabaseConnection
from Models.Project import Project
from Models.EventListener import EventListener
import codecs

from Models.Version import Version


class ProjectModel(EventListener):
    def __init__(self):
        super().__init__()
        self.project = None
        self.versions = []

    def set_project(self, project: Project):
        self.project = project

    def load_versions(self):
        self.versions.clear()
        connection = DatabaseConnection()
        query = f"SELECT * FROM versions WHERE project_id = {self.project.project_id};"
        cursor = connection.get_cursor_query(query)
        versions = cursor.fetchall()
        for item in versions:
            version = Version(item[0], item[1], item[2], item[3], item[4])
            self.versions.append(version)

    def get_versions(self):
        return self.versions

    def open_version_project(self):
        self.trigger_event("open_version_creator")

    def open_file(self, file):
        path = self.project.local_path + "\\" + file
        file = codecs.open(path, encoding='utf-8')
        return file.read()
