import ipdb
from models.__init__ import CONN, CURSOR


class Example:

    all = []

    def __init__(self, name):
        self.name = name
        self.id = None

    # @property
    # def name(self):
    #     self._name
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE examples (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        '''

        CURSOR.execute(sql)
    
    def save(self):
        sql = """
            INSERT INTO examples (name) VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Example.all.append(self)
ipdb.set_trace()