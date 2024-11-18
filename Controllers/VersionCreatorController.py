class VersionCreatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_binds(self._bind, "version_creator")

    def create_version(self):
        self.model.version_creator.create_version()

    def _bind(self, frame):
        frame.create_button.config(command=self.create_version)
