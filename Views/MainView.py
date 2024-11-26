from Views.ProjectManagerView import ProjectManagerView
from Views.PasswordView import PasswordView
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
        self.current_dialog = None
        self.current_dialog_fields = {}
        self.current_frame_fields = {}

        self.add_window(ProjectManagerView, "project_manager")
        self.add_window(PasswordView, "password")
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
        self.current_dialog = self.windows[view_name](self.parent)
        self.current_dialog_fields.clear()
        self.current_dialog_fields = self.current_dialog.get_fields()
        if view_name in self.binds.keys():
            self.binds[view_name](self.current_dialog)
        self.current_dialog.grab_set()

    def close_dialog(self):
        if self.current_dialog is not None:
            self.current_dialog.destroy()
            self.current_dialog = None

    def get_field(self, name):
        if name in self.current_frame_fields.keys():
            return self.current_frame_fields[name]
        if name in self.current_dialog_fields.keys():
            return self.current_dialog_fields[name]
        return None

    def show_message(self, title, message):
        messagebox.showwarning(title, message)

    def wait_window(self, window):
        self.parent.wait_window(window)

    def start_loop(self):
        self.parent.mainloop()
