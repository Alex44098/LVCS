import os
from Models.DatabaseConnection import DatabaseConnection


def get_files_list(file_list: list, path):
    for i in os.listdir(path):
        if os.path.isdir(f"{path}/{i}"):
            get_files_list(file_list, f"{path}/{i}")
        else:
            file_list.append(f"{path}/{i}")


def check_file_extension(extension, project):
    connection = DatabaseConnection()
    request = 'SELECT language_id FROM project_info WHERE info_id = ' + str(project.info_id) + ';'
    cursor = connection.get_cursor_query(request)
    lang_id = cursor.fetchall()

    request = 'SELECT ext FROM lang_exts WHERE lang_id = ' + str(lang_id[0][0]) + ';'
    cursor = connection.get_cursor_query(request)
    exts = cursor.fetchall()

    for ext in exts:
        if extension == ext[0]:
            return True
    return False
