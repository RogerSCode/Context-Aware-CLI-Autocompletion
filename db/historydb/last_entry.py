import sqlite3

connection = sqlite3.connect('db/historydb/history.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM history ORDER BY Date DESC LIMIT 1")
row = cursor.fetchone()
print(row[2])