import sqlite3
con = sqlite3.connect("database.db")
#con = sqlite3.connect(':memory:') #to create Temporary Database that auto deleted
c = con.cursor()

c.execute("CREATE TABLE IF NOT EXISTS names(fname TEXT, lname TEXT, age INT, salary REAL);")
c.execute("INSERT INTO names VALUES('OSAMA', 'MOHAMED', 23, 2000);")
con.commit()

con.close()
