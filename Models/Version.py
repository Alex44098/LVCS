class Version:
    def __init__(self, version_id, project_id, name, description, prev_version):
        self.version_id = version_id
        self.project_id = project_id
        self.name = name
        self.description = description
        self.prev_version = prev_version
