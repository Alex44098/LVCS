from tkinter import Tk

from Models.MainModel import MainModel
from Views.MainView import MainView
from Controllers.MainController import MainController
from Utils.DatabaseIntializer import init_database


if __name__ == '__main__':
    root = Tk()
    root.withdraw()

    init_database()

    model = MainModel()
    view = MainView(root)
    controller = MainController(model, view)

    controller.start()
