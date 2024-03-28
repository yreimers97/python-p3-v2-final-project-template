from models.__init__ import CONN, CURSOR
import ipdb


class Review:

    all = []

    def __init__(self, rating, text, job_id):
        self.rating = rating
        self.text = text
        self.job_id = job_id
        self.id = None

    @property
    def hotel_id(self):
        return self._job_id
    
    @job_id.setter
    def job_id(self, job_id_parameter):
        print(job_id_parameter)

    
    @classmethod
    def create_table(cls):
    
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            rating INTEGER,
            text TEXT,
            job_id INTEGER)
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO reviews (rating, text, job_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.rating, self.text, self.job_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Review.all.append(self)


ipdb.set_trace()