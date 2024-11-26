from Controllers.ProjectController import ProjectController
from Controllers.ProjectCreatorController import ProjectCreatorController
from Controllers.ProjectManagerController import ProjectManagerController
from Controllers.VersionCreatorController import VersionCreatorController
from Controllers.PasswordController import PasswordController
from Models import MainModel
from Views import MainView


class MainController:
    def __init__(self, model: MainModel, view: MainView):
        self.view = view
        self.model = model
        self.project_manager_controller = ProjectManagerController(model, view)
        self.password_controller = PasswordController(model, view)
        self.project_creator_controller = ProjectCreatorController(model, view)
        self.project_controller = ProjectController(model, view)
        self.version_creator_controller = VersionCreatorController(model, view)

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
        self.model.project.add_listener(
            "open_version_creator", self.open_version_creator
        )

    def open_creator_listener(self):
        self.view.switch_view("project_creator")
        self.project_creator_controller.init_creator()

    def check_password(self):
        if self.password_controller.project_has_password():
            self.view.show_view_as_dialog("password")
            # Waiting for password
            self.view.wait_window(self.view.current_dialog)
            return self.password_controller.password_is_ok
        return True

    def open_project_listener(self):
        if self.check_password():
            self.view.switch_view("project")
            self.project_controller.open_project(self.model.current_project)
        else:
            self.view.show_message("Ошибка", "Неверный пароль!")

    def open_project_manager(self):
        self.view.switch_view("project_manager")
        self.project_manager_controller.init_manager()

    def open_version_creator(self):
        self.view.show_view_as_dialog("version_creator")

    def start(self):
        self.open_project_manager()
        self.view.start_loop()
