from Models.ProjectManagerModel import ProjectManagerModel
from Models.ProjectCreatorModel import ProjectCreatorModel


class MainModel:
    def __init__(self):
        self.project_manager = ProjectManagerModel()
        self.project_creator = ProjectCreatorModel()
