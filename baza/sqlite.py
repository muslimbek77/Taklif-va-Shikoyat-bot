import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS USERS(
        full_name TEXT,
        telegram_id NUMBER unique );
              """
        self.execute(sql, commit=True)
    
    def create_table_channels(self):
        sql = """
    CREATE TABLE IF NOT EXISTS Channels (
    channel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    channel_name TEXT NOT NULL,
    channel_link TEXT NOT NULL);
                """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


    def add_user(self, telegram_id:int, full_name:str):

        sql = """
        INSERT INTO Users(telegram_id, full_name) VALUES(?, ?);
        """
        return self.execute(sql, parameters=(telegram_id, full_name), commit=True)

    def add_chanel(self, chanel_id, chanel_name, chanel_link):
        sql = "INSERT INTO Channels (channel_id, channel_name, channel_link) VALUES(?, ?,?);"
        return self.execute(sql, parameters=(chanel_id, chanel_name, chanel_link), commit=True)
    
    def select_all_channels(self):
        sql = "SELECT * FROM Channels"
        return self.execute(sql, fetchall=True)

    def delete_channel(self, id ):
        self.execute(f"DELETE FROM Channels WHERE channel_id = ?",parameters=(id,), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users;
        """
        return self.execute(sql, fetchall=True)


    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE;"
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)


    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE;", commit=True)
    
    def all_users_id(self):
        return self.execute("SELECT telegram_id FROM Users;", fetchall=True)

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")