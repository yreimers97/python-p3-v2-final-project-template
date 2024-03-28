import sqlite3

CONN = sqlite3.connect('job_reviews.db')
CURSOR = CONN.cursor()
