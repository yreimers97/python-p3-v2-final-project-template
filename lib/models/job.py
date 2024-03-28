from models.__init__ import CONN, CURSOR
import ipdb

class Job:

    all = []

    def __init__(self, title, salary ):
        self.title = title
        self.salary = salary
        self.id = None

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title_parameter):
        if(type(title_parameter, str)) and (len(title_parameter) > 0):
            self._title = title_parameter
        else:
            raise ValueError("Title must be a string")
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary_parameter):
        if(type(salary_parameter, int)) and ((salary_parameter) > 0):
            self._salary = salary_parameter
        else:
            raise ValueError("Salary must be an integer")
        
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS jobs  (
                id INTEGER PRIMARY KEY,
                title TEXT,
                avg_salary INTEGER 
            )
        '''

        CURSOR.execute(sql)
    
    def save(self):
        sql = """
            INSERT INTO jobs (title, salary) VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.title, self.salary))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Job.all.append(self)

    def delete(self):
        sql = """
            DELETE FROM jobs WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

ipdb.set_trace()



