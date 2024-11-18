from Models.EventListener import EventListener


class VersionCreatorModel(EventListener):
    def __init__(self):
        super().__init__()

    def create_model(self):
        print("Yes")
