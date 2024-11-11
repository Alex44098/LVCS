class ProjectCreatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_binds(self._bind, "project_creator")

    def create_new_project(self):
        self.model.project_creator.create_project()

    def close_creator(self):
        self.model.project_creator.close_creator()

    def _bind(self, frame):
        frame.create_button.config(command=self.create_new_project)
        frame.cancel_button.config(command=self.close_creator)

