from Models.Project import Project
from Models.DatabaseConnection import DatabaseConnection
from Models.EventListener import EventListener
import codecs


class ProjectModel(EventListener):
    def __init__(self):
        super().__init__()
        self.project = None

    def set_project(self, project: Project):
        self.project = project

    def check_file_extension(self, extension):
        connection = DatabaseConnection()
        request = 'SELECT language_id FROM project_info WHERE info_id = ' + str(self.project.info_id) + ';'
        cursor = connection.get_cursor_query(request)
        lang_id = cursor.fetchall()

        request = 'SELECT ext FROM lang_exts WHERE lang_id = ' + str(lang_id[0][0]) + ';'
        cursor = connection.get_cursor_query(request)
        exts = cursor.fetchall()

        for ext in exts:
            if extension == ext[0]:
                return True
        return False

    def open_file(self, file):
        path = self.project.local_path + "\\" + file
        file = codecs.open(path, encoding='utf-8')
        return file.read()
