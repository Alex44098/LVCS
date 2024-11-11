from Views.ProjectManagerView import ProjectManagerView
from Views.ProjectCreatorView import ProjectCreatorView
from Views.ProjectView import ProjectView


class MainView:
    def __init__(self, parent):
        self.parent = parent
        self.frames = {}
        self.binds = {}
        self.current_frame = None

        self.add_window(ProjectManagerView, "project_manager")
        self.add_window(ProjectCreatorView, "project_creator")
        self.add_window(ProjectView, "project")

    def add_window(self, window, name):
        self.frames[name] = window

    def add_binds(self, bind, name):
        self.binds[name] = bind

    def switch(self, name):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = self.frames[name](self.parent)
        if name in self.binds.keys():
            self.binds[name](self.current_frame)

    def start_loop(self):
        self.parent.mainloop()
