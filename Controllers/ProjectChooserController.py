class ProjectChooserController(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_item(self):
        self.view.add_item("Aboba")