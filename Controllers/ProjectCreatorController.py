class ProjectCreatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_binds(self._bind, "project_creator")

    def init_creator(self):
        lang_combobox = self.view.get_field("lang_combobox")
        langs = self.model.project_creator.get_languages()
        lang_names = []
        for lang in langs:
            lang_names.append(lang[1])
        lang_combobox['values'] = lang_names

    def create_new_project(self):
        name_text = self.view.get_field("name_text")
        path_text = self.view.get_field("path_text")
        lang_combobox = self.view.get_field("lang_combobox")
        description_text = self.view.get_field("description_text")
        password_text = self.view.get_field("password_text")

        new_project = self.model.project_creator.create_project(name_text.get(), path_text.cget('text'),
                                                                description_text.get("1.0", "end"),
                                                                lang_combobox.get(), password_text.get())
        self.model.set_project(new_project)
        self.model.project_creator.project_created()

    def close_creator(self):
        self.model.project_creator.close_creator()

    def _bind(self, frame):
        frame.create_button.config(command=self.create_new_project)
        frame.cancel_button.config(command=self.close_creator)
