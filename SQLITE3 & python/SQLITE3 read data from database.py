import sqlite3
con = sqlite3.connect("database.db")
c = con.cursor()

c.execute("SELECT * FROM names")
for row in c.fetchall():
    print(row)

con.close()
