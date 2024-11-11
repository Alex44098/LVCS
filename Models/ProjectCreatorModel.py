from Models.EventListener import EventListener


class ProjectCreatorModel(EventListener):
    def __init__(self):
        super().__init__()

    def create_project(self):
        self.trigger_event("create_project")

    def close_creator(self):
        self.trigger_event("close_creator")
