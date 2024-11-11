class ProjectManagerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_binds(self._bind, "project_manager")

    def create_project(self):
        self.model.project_manager.open_creator()

    def open_project(self):
        self.model.project_manager.open_project()

    def _bind(self, frame):
        frame.Button_create.config(command=self.create_project)
        frame.Button_open.config(command=self.open_project)
