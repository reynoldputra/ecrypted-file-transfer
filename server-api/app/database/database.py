import sqlite3

connection = sqlite3.connect("db.sqlite3")

print(connection.total_changes)

cursor = connection.cursor()

def dbCreate(query : str):
    cursor.execute(query)

def debGet(query : str):
    rows = cursor.execute(query).fetchall()
    return rows

connection.commit()
connection.close()
