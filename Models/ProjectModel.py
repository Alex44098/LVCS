from Models.EventListener import EventListener
import codecs


class ProjectModel(EventListener):
    def __init__(self):
        super().__init__()

    def open_file(self, path):
        file = codecs.open(path, encoding='utf-8')
        return file.read()
