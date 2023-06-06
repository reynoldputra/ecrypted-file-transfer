import sqlite3

connection = sqlite3.connect("db.sqlite3")

def dbCreate(query : str):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

def dbGet(query : str):
    cursor = connection.cursor()
    rows = cursor.execute(query).fetchall()
    connection.commit()
    return rows

