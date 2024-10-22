class ProjectManagerModel(object):
    def __init__(self, connection):
        self.connection = connection

    def get_projects(self):
        request = """SELECT * FROM projects;"""
        cursor = self.connection.cursor()
        cursor.execute(request)
        projects = cursor.fetchall()

        for project in projects:
            yield project
