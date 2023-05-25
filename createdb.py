import sqlite3

connnection = sqlite3.connect('history.db')
cursor = connnection.cursor()

cursor.execute('''create table history(
        id INTEGER PRIMARY KEY,
        Path TEXT not null,
        Command TEXT not null,
        Date TEXT not null
        )''')
connnection.commit()
connnection.close()