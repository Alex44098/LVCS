class ProjectManagerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_binds(self._bind, "project_manager")

        self.projects = []

    def init_manager(self):
        listbox = self.view.get_field("projects_listbox")
        self.projects = self.model.project_manager.get_projects()
        for project in self.projects:
            listbox.insert(0, project.name)

    def open_creator(self):
        self.model.project_manager.open_creator()

    def open_project(self):
        listbox = self.view.get_field("projects_listbox")
        self.model.set_project(self.projects[len(self.projects) - listbox.curselection()[0] - 1])
        self.model.project_manager.open_project()

    def _bind(self, frame):
        frame.Button_create.config(command=self.open_creator)
        frame.Button_open.config(command=self.open_project)
