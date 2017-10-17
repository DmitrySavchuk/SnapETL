import sqlite3
import csv
import sys


csv_file = sys.argv[1]
db_file = '../job_db.sqlite3'   # database is located in the top level directory

conn = sqlite3.connect(db_file)
db = conn.cursor()

create_table = """CREATE TABLE IF NOT EXISTS jobs (Title text NOT NULL, Category text NOT NULL,
                                                    Status text NOT NULL, Location text NOT NULL
                                    );"""
erase_table = """DELETE FROM jobs"""

db.execute(create_table)
db.execute(erase_table)


with open(csv_file, "r", newline='') as in_file:
    csv_reader = csv.reader(in_file, delimiter=',')

    for row in csv_reader:
        db.execute('INSERT INTO  jobs VALUES (?,?,?,?)', row)


conn.commit()
conn.close()
