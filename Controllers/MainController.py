from Models import ProjectManagerModel
from Views import ProjectManagerView, ProjectView, ProjectCreatorView


class ProjectChooserController(object):
    def __init__(self, conn, root):
        self.root = root
        self.model = ProjectManagerModel.ProjectManagerModel(conn)
        self.view = None
        self.create_project_manager_view()

    def open_project(self):
        self.create_project_view()

    def create_new_project(self):
        self.create_project_creator_view()

    def create_project_manager_view(self):
        if self.view is not None:
            self.view.withdraw()
        self.view = ProjectManagerView.ProjectManagerView(self.root)
        self.view.Button_create.config(command=self.create_new_project)
        self.view.Button_open.config(command=self.open_project)

    def create_project_creator_view(self):
        creator_view = ProjectCreatorView.ProjectCreatorView(self.root)
        creator_view.grab_set()
        creator_view.create_button.config(command=self.create_project_view)

    def create_project_view(self):
        if self.view is not None:
            self.view.withdraw()
        self.view = ProjectView.ProjectView(self.root, "../")
