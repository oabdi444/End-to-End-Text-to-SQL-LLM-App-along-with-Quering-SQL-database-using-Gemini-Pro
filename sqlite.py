import sqlite3

## Connect to SQlite
connection=sqlite3.connect("student1.db")

## Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""
cursor.execute(table_info)

## Inser some more records

cursor.execute("Insert into STUDENT values('Krish','Data Science','A',90);")
cursor.execute("Insert into STUDENT values('YUSUF','Data Science','A',85);")
cursor.execute("Insert into STUDENT values('Darius','Data Science','A',97);")
cursor.execute("Insert into STUDENT values('Osman','DevOps','A',70);")
cursor.execute("Insert into STUDENT values('Abdi','DevOps','A',80);")

## Display All the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## commit your changes int the database
connection.commit()
connection.close()