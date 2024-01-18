import sqlite3


class DB:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

    def create(self, name, **kwargs):
        columns = 'id INT PRIMARY KEY,'

        for i in kwargs:
            columns += i + ' ' + kwargs[i] + ','
        try:
            self.cursor.execute(f"""CREATE TABLE {name} ({columns});""")
        except sqlite3.OperationalError:
            print('Table already exists')
        self.connection.commit()

    def insert(self, name, data):  # data - 2-dim list [[1, 2, 3]]
        for i in data:
            q = ('?,' * len(i))[:-1]
            self.cursor.executemany(f"""INSERT INTO {name} VALUES({q})""", [tuple(i)])
        self.connection.commit()

    def update(self, name, condition, **kwargs):
        for i in kwargs:
            self.cursor.execute(f"""UPDATE {name} SET {i} = '{kwargs[i]}' WHERE {condition}""")
        self.connection.commit()

    def delete(self, name, condition, ):
        self.cursor.execute(f"""DELETE FROM {name} WHERE {condition}""")
        self.connection.commit()

    def select(self, name):
        self.cursor.execute(f"""SELECT * FROM {name}""")
        return self.cursor.fetchall()

    def __del__(self):
        self.connection.commit()
        self.connection.close()

