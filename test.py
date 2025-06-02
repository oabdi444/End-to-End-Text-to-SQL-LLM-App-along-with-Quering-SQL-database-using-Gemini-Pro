import sqlite3

conn=sqlite3.connect('student.db')
cur=conn.cursor()
cur.execute("Select * from STUDENT")
rows=cur.fetchall()
print(rows)
for row in rows:
        
    print(row)