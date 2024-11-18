import os
import Models.ProjectFileManager as ProjectFileManager
from Models.Project import Project


class ProjectController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_binds(self._bind, "project")

    def open_project(self, project: Project):
        self.model.project.set_project(project)
        self.view.current_frame.set_project_path(project.local_path)
        self.model.project.load_versions()
        version_label = self.view.get_field("version_label")
        version_label.config(text=self.model.project.get_current_version_name())
        self.set_versions()

    def open_version_creator(self):
        self.model.project.open_version_project()

    def set_versions(self):
        versions_combobox = self.view.get_field("versions_combobox")
        versions = self.model.project.get_versions()
        versions_names = []
        for version in versions:
            versions_names.append(version.name)
        versions_combobox['values'] = versions_names

    def open_file(self):
        file_tree = self.view.get_field("file_tree")
        item = file_tree.focus()

        ext = os.path.splitext(file_tree.item(item)['text'])[-1]
        if not ProjectFileManager.check_file_extension(ext[1:], self.model.current_project):
            self.view.show_message("Внимание", "Данный файл не является файлом языка проекта")
            return

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
        frame.new_version_button.config(command=self.open_version_creator)
