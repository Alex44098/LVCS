class VersionCreatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_binds(self._bind, "version_creator")

    def create_version(self):
        name_entry = self.view.get_field("name_text")
        desc_entry = self.view.get_field("desc_text")
        self.model.version_creator.create_version(self.model.current_project, name_entry.get(),
                                                  desc_entry.get("1.0", "end"))
        self.view.close_dialog()

    def _bind(self, frame):
        frame.create_button.config(command=self.create_version)
