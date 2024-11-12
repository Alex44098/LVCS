import os
from Models.Project import Project


class ProjectController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_binds(self._bind, "project")

    def open_project(self, project: Project):
        self.model.project.set_project(project)
        self.view.current_frame.set_project_path(project.local_path)

    def open_file(self):
        file_tree = self.view.get_field("file_tree")
        item = file_tree.focus()
        parent_iid = file_tree.parent(item)
        node = []
        while parent_iid != '':
            node.insert(0, file_tree.item(parent_iid)['text'])
            parent_iid = file_tree.parent(parent_iid)
        i = file_tree.item(item, "text")
        path = os.path.join(*node, i)

        text_file = self.model.project.open_file(path)

        text_field = self.view.get_field("text_field")
        text_field.delete("1.0", "end")
        text_field.insert("1.0", text_file)

    def _bind(self, frame):
        frame.open_file_button.config(command=self.open_file)
