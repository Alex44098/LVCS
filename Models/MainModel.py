from Models.ProjectManagerModel import ProjectManagerModel
from Models.ProjectCreatorModel import ProjectCreatorModel
from Models.ProjectModel import ProjectModel


class MainModel:
    def __init__(self):
        self.project_manager = ProjectManagerModel()
        self.project_creator = ProjectCreatorModel()
        self.project = ProjectModel()
