from Views.ProjectManagerView import ProjectManagerView
from Views.ProjectCreatorView import ProjectCreatorView
from Views.ProjectView import ProjectView


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

    def add_window(self, window, name):
        self.windows[name] = window

    def add_binds(self, bind, name):
        self.binds[name] = bind

    def switch(self, name):
        self.current_frame_fields.clear()
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = self.windows[name](self.parent)
        self.current_frame_fields = self.current_frame.get_fields()
        if name in self.binds.keys():
            self.binds[name](self.current_frame)

    def get_field(self, name):
        if name in self.current_frame_fields.keys():
            return self.current_frame_fields[name]
        else:
            print(name + " in " + type(self.current_frame) + " doesnt exist!")

    def start_loop(self):
        self.parent.mainloop()
