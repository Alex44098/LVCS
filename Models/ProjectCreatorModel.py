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
                "(\"" + description +\
                "\", (SELECT language_id FROM languages WHERE name = \"" + language_name + "\"), \"" \
                + password + "\");"

        info_id = connection.execute_query(query)

        query = "INSERT INTO projects (name, local_path, info_id) VALUES (\"" + name + "\", \"" + path +\
                "\", " + str(info_id) + ")"
        project_id = connection.execute_query(query)

        return Project(project_id, name, path, info_id)

    def project_created(self):
        self.trigger_event("create_project")

    def close_creator(self):
        self.trigger_event("close_creator")
