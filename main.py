from tkinter import Tk
from Views import ProjectManagerView
from Controllers import ProjectManagerController
from Models import ProjectManagerModel
import sqlite3


def init_database(name):
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    local_path TEXT NOT NULL,
    info_id INTEGER);''')
    connection.commit()
    return connection


if __name__ == '__main__':
    connection = init_database("database.db")
    root = Tk()
    root.withdraw()

    project_manager_controller = ProjectManagerController.ProjectChooserController(connection, root)
    root.mainloop()

    connection.close()
