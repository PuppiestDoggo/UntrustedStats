import sqlite3


def addUser(user):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users VALUES (?)", user)
    connection.commit()
    cursor.close()
    connection.close()

def listUsers():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Username from Users")
    val = cursor.fetchall()
    cursor.close()
    connection.close()
    return val
