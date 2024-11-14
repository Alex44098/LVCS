import os
import codecs

import Models.ProjectFileManager as ProjectFileManager

from Models.EventListener import EventListener
from Models.DatabaseConnection import DatabaseConnection
from Models.Project import Project


class ProjectCreatorModel(EventListener):
    def __init__(self):
        super().__init__()

    def get_languages(self):
        connection = DatabaseConnection()
        request = 'SELECT * FROM languages'
        cursor = connection.get_cursor_query(request)
        langs = cursor.fetchall()

        return langs

    def create_project(self, name, path, description, language_name, password):
        connection = DatabaseConnection()

        query = "INSERT INTO project_info (description, language_id, password) VALUES" \
                "(\"" + description + \
                "\", (SELECT language_id FROM languages WHERE name = \"" + language_name + "\"), \"" \
                + password + "\");"

        info_id = connection.execute_query(query)

        query = "INSERT INTO projects (name, local_path, info_id) VALUES (\"" + name + "\", \"" + path + \
                "\", " + str(info_id) + ")"
        project_id = connection.execute_query(query)

        return Project(project_id, name, path, info_id)

    def create_first_version(self, project: Project):
        connection = DatabaseConnection()
        query = "INSERT INTO versions (project_id, version_name, description) VALUES (" + str(project.project_id) +\
                ", \"v0.1\", \"First version.\");"
        version_id = connection.execute_query(query)

        file_list = []
        ProjectFileManager.get_files_list(file_list, project.local_path)

        for file in file_list:
            ext = os.path.splitext(file)[-1]
            if ProjectFileManager.check_file_extension(ext[1:], project):
                file_text = codecs.open(file, encoding='utf-8').read()
                file_text = file_text.replace("'", "''")
                query = f"INSERT INTO versions_diff (version_id, file_name, diff) VALUES ({version_id}"\
                        f", \' {file} \', \' {file_text} \');"
                connection.execute_query(query)

    def project_created(self):
        self.trigger_event("create_project")

    def close_creator(self):
        self.trigger_event("close_creator")
