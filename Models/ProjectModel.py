from Models.DatabaseConnection import DatabaseConnection
from Models.Project import Project
from Models.EventListener import EventListener
import codecs
import difflib as df

from Models.Version import Version


class ProjectModel(EventListener):
    def __init__(self):
        super().__init__()
        self.project = None
        self.current_version = None
        self.versions = []

    def set_project(self, project: Project):
        self.project = project

    def set_version_by_name(self, version_name):
        self.current_version = None
        if version_name == "Локальная":
            return
        for version in self.versions:
            if version.name == version_name:
                self.current_version = version
        if self.current_version is None:
            print("Wrong version!")

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
        path = self.project.local_path + "/" + file
        if self.current_version is None:
            file = codecs.open(path, encoding='utf-8')
            return file.read()
        else:
            try:
                path = path.replace('\\', '/')
                text = self.get_file_by_name(self.current_version.version_id, path)
                return text
            except FileExistsError:
                return "Файл в этой версии не существовал."

    def get_file_by_name(self, version_id, name):
        connection = DatabaseConnection()
        query = f"SELECT diff, first_version FROM versions_diff WHERE " \
                f"version_id = {version_id} AND file_name = \'{name}\';"
        cursor = connection.get_cursor_query(query)
        file = cursor.fetchall()
        if len(file) == 0:
            raise FileExistsError
        if file[0][1] == 0:
            diff = list()
            for i in range(0, len(file[0][0]), 3):
                new_item = file[0][0][i] + file[0][0][i + 1] + file[0][0][i + 2]
                diff.append(new_item)
            return ''.join(df.restore(diff, 2))
        return file[0][0]
