import sqlite3
con = sqlite3.connect("database.db")
c = con.cursor()

c.execute("UPDATE names SET fname='OSAMA', lname='MOHAMED', age=22, salary=5000 WHERE age=20")
con.commit()
con.close()
