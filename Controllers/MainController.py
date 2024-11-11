from Controllers.ProjectCreatorController import ProjectCreatorController
from Controllers.ProjectManagerController import ProjectManagerController
from Models import MainModel
from Views import MainView


class MainController:
    def __init__(self, model: MainModel, view: MainView):
        self.view = view
        self.model = model
        self.project_manager_controller = ProjectManagerController(model, view)
        self.project_creator_controller = ProjectCreatorController(model, view)

        self.model.project_manager.add_listener(
            "open_creator", self.open_creator_listener
        )
        self.model.project_manager.add_listener(
            "open_project", self.open_project_listener
        )
        self.model.project_creator.add_listener(
            "create_project", self.open_project_listener
        )

        self.model.project_creator.add_listener(
            "close_creator", self.open_project_manager
        )

    def open_creator_listener(self):
        self.view.switch("project_creator")

    def open_project_listener(self):
        self.view.switch("project")

    def open_project_manager(self):
        self.view.switch("project_manager")

    def start(self):
        self.open_project_manager()
        self.view.start_loop()
