import sqlite3
import sys
from datetime import datetime

path = sys.argv[1]
command = sys.argv[2]
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')



connnection = sqlite3.connect('db/historydb/history.db')
cursor = connnection.cursor()

cursor.execute('''insert into history(Path, Command, Date) values(?,?,?)''', (path, command, date))
connnection.commit()
connnection.close()