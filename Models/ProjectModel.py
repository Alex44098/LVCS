from Models.Project import Project

from Models.EventListener import EventListener
import codecs


class ProjectModel(EventListener):
    def __init__(self):
        super().__init__()
        self.project = None

    def set_project(self, project: Project):
        self.project = project

    def open_file(self, file):
        path = self.project.local_path + "\\" + file
        file = codecs.open(path, encoding='utf-8')
        return file.read()

