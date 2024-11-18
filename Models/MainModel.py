from Models.Project import Project
from Models.ProjectManagerModel import ProjectManagerModel
from Models.ProjectCreatorModel import ProjectCreatorModel
from Models.ProjectModel import ProjectModel
from Models.VersionCreatorModel import VersionCreatorModel


class MainModel:
    def __init__(self):
        self.project_manager = ProjectManagerModel()
        self.project_creator = ProjectCreatorModel()
        self.project = ProjectModel()
        self.version_creator = VersionCreatorModel()

        self.current_project = None

    def set_project(self, project: Project):
        self.current_project = project
