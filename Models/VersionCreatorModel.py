import difflib as df
import os
import codecs

from Models.DatabaseConnection import DatabaseConnection
from Models.EventListener import EventListener
import Models.ProjectFileManager as ProjectFileManager
from Models.Version import Version


class VersionCreatorModel(EventListener):
    def __init__(self):
        super().__init__()

    def create_version(self, project, name, desc):
        connection = DatabaseConnection()
        last_version = self.get_last_version(project.project_id)

        query = "INSERT INTO versions (project_id, version_name, description, prev_version) VALUES" \
                f"({project.project_id}, \'{name}\', \'{desc}\', {last_version.version_id})"
        new_version_id = connection.execute_query(query)
        self.create_file_diffs(last_version.version_id, new_version_id, project)

    def create_file_diffs(self, last_version_id, new_version_id, project):
        connection = DatabaseConnection()

        file_list = []
        ProjectFileManager.get_files_list(file_list, project.local_path)

        # Look up all files in local directory
        for file in file_list:
            ext = os.path.splitext(file)[-1]
            # Check for supported extensions
            if ProjectFileManager.check_file_extension(ext[1:], project):
                # Read local file
                current_file = codecs.open(file, encoding='utf-8').read()
                # Try to find local file in database
                try:
                    last_version_file = self.get_file_by_name(last_version_id, file)
                    # Creating list of difference between two files
                    diff = list(df.ndiff(last_version_file, current_file))
                    # Convert diff list to string for database
                    str_diff = ""
                    for item in diff:
                        str_diff += item
                    str_diff = str_diff.replace("'", "''")
                    query = "INSERT INTO versions_diff (version_id, file_name, diff, first_version) VALUES" \
                            f"({new_version_id}, \'{file}\', \'{str_diff}\', 0)"
                    connection.execute_query(query)
                # Create new file entry for database
                except FileExistsError:
                    current_file = current_file.replace("'", "''")
                    query = "INSERT INTO versions_diff (version_id, file_name, diff, first_version) VALUES" \
                            f"({new_version_id}, \'{file}\', \'{current_file}\', 1)"
                    connection.execute_query(query)

    def get_last_version(self, project_id):
        connection = DatabaseConnection()
        query = f"SELECT * FROM versions WHERE project_id = {project_id} " \
                f"ORDER BY version_id DESC LIMIT 1"
        cursor = connection.get_cursor_query(query)
        ver = cursor.fetchall()
        if len(ver) > 0:
            version = Version(ver[0][0], ver[0][1], ver[0][2], ver[0][3], ver[0][4])
            return version

    def get_file_by_name(self, version_id, name):
        connection = DatabaseConnection()
        query = f"SELECT diff, first_version FROM versions_diff WHERE " \
                f"version_id = {version_id} AND file_name = \'{name}\';"
        cursor = connection.get_cursor_query(query)
        file = cursor.fetchall()
        if len(file) == 0:
            raise FileExistsError
        if file[0][1] == 0:
            diff = list()
            for i in range(0, len(file[0][0]), 3):
                new_item = file[0][0][i] + file[0][0][i + 1] + file[0][0][i + 2]
                diff.append(new_item)
            return ''.join(df.restore(diff, 2))
        return file[0][0]
