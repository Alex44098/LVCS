from tkinter import Tk
# from Views import ProjectManagerView
from Controllers import MainController
# from Models import ProjectManagerModel
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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS project_info (
        info_id INTEGER PRIMARY KEY,
        description TEXT NOT NULL,
        language_id INTEGER NOT NULL,
        password TEXT);''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS languages (
        language_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL);''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS versions (
        version_id INTEGER PRIMARY KEY,
        project_id INTEGER NOT NULL,
        info_id INTEGER NOT NULL);''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS versions_info (
        info_id INTEGER PRIMARY KEY,
        description TEXT NOT NULL,
        diff_file_path TEXT NOT NULL);''')

    connection.commit()
    return connection


if __name__ == '__main__':
    connection = init_database("database.db")
    root = Tk()
    root.withdraw()

    project_manager_controller = MainController.ProjectChooserController(connection, root)
    root.mainloop()

    connection.close()
