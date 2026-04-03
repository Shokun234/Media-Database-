import sqlite3

connection = sqlite3.connect("Table.db")
cursor = connection.execute("") #Do in this
for row in cursor:
    print("")