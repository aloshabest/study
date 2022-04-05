import sqlite3

conn = sqlite3.connect("students_py.db")
c = conn.cursor()

#c.execute("CREATE TABLE students_py (name TEXT, last_name TEXT, age TEXT);")
c.execute("INSERT INTO students_py VALUES ('Lil', 'Wane', '22');")

conn.commit()

conn.close()