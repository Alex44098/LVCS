from Models.DatabaseConnection import DatabaseConnection


def init_database():
    projects = '''
        CREATE TABLE IF NOT EXISTS projects (
        project_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        local_path TEXT NOT NULL,
        info_id INTEGER);'''

    projects_info = '''
        CREATE TABLE IF NOT EXISTS project_info (
        info_id INTEGER PRIMARY KEY,
        description TEXT NOT NULL,
        language_id INTEGER NOT NULL,
        password TEXT);'''

    languages = '''
        CREATE TABLE IF NOT EXISTS languages (
        language_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL);'''

    lang_exts = '''
        CREATE TABLE IF NOT EXISTS lang_exts (
        ext_id INTEGER PRIMARY KEY,
        lang_id INTEGER,
        ext TEXT);'''

    versions = '''
        CREATE TABLE IF NOT EXISTS versions (
        version_id INTEGER PRIMARY KEY,
        project_id INTEGER NOT NULL,
        version_name TEXT NOT NULL,
        description TEXT,
        prev_version INTEGER);'''

    version_diff = '''
        CREATE TABLE IF NOT EXISTS versions_diff (
        diff_id INTEGER PRIMARY KEY,
        version_id INTEGER NOT NULL,
        file_name TEXT NOT NULL,
        diff TEXT NOT NULL);'''

    connection = DatabaseConnection()

    connection.execute_query(projects)
    connection.execute_query(projects_info)
    connection.execute_query(languages)
    connection.execute_query(lang_exts)
    connection.execute_query(versions)
    connection.execute_query(version_diff)
