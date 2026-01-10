# Singleton Pattern for Database Connection
class DatabaseConnection:
    _instance = None

    def __new__(cls, db_path):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(db_path)
        return cls._instance

    def get_connection(self):
        return self.connection
