from Models import ProjectManagerModel
from Views import ProjectManagerView


class ProjectChooserController(object):
    def __init__(self, conn, root):
        self.model = ProjectManagerModel.ProjectManagerModel(conn)
        self.view = ProjectManagerView.ProjectManagerView(root)
        self.view.set_ctrl(self)

    def open_project(self):
        self.view.add_item("Aboba")

    def create_new_project(self):
        pass
