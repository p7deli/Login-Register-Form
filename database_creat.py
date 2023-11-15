from sqlite3 import connect


class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.db = None

    def connect_db(self):
        self.db = connect(self.database_name)

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS my_user (
            Id_ INTEGER PRIMARY KEY AUTOINCREMENT,
            First_name TEXT,
            Last_name TEXT,
            User_name TEXT,
            Password TEXT
            )
        """)

    def close_db(self):
        self.db.close()

    def check_user(self, username, password):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT * FROM my_user WHERE User_name=? AND Password=?
        """, (username, password))
        table_info = cursor.fetchall()
        if len(table_info) == 0:
            return True
        return False

    def create_user(self, firstname, lastname, username, password):
        if self.check_user(username, password):
            cursor = self.db.cursor()
            cursor.execute(f"""
                INSERT INTO my_user (First_name, Last_name, User_name, Password)
                VALUES (?, ?, ?, ?)
            """, (firstname, lastname, username, password))
            self.db.commit()
            return True
        return False
