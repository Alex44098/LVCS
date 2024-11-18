from Views.ProjectManagerView import ProjectManagerView
from Views.ProjectCreatorView import ProjectCreatorView
from Views.ProjectView import ProjectView
from tkinter import messagebox

from Views.VersionCreatorView import VersionCreatorView


class MainView:
    def __init__(self, parent):
        self.parent = parent
        self.windows = {}
        self.binds = {}

        self.current_frame = None
        self.current_frame_fields = {}

        self.add_window(ProjectManagerView, "project_manager")
        self.add_window(ProjectCreatorView, "project_creator")
        self.add_window(ProjectView, "project")
        self.add_window(VersionCreatorView, "version_creator")

    def add_window(self, window, name):
        self.windows[name] = window

    def add_binds(self, bind, name):
        self.binds[name] = bind

    def switch_view(self, name):
        self.current_frame_fields.clear()
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = self.windows[name](self.parent)
        self.current_frame_fields = self.current_frame.get_fields()
        if name in self.binds.keys():
            self.binds[name](self.current_frame)

    def show_view_as_dialog(self, view_name):
        view = self.windows[view_name](self.parent)
        view.grab_set()

    def get_field(self, name):
        if name in self.current_frame_fields.keys():
            return self.current_frame_fields[name]
        else:
            print(name + " in " + type(self.current_frame) + " doesnt exist!")

    def show_message(self, title, message):
        messagebox.showwarning(title, message)

    def start_loop(self):
        self.parent.mainloop()
