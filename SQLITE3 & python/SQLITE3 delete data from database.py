import sqlite3
con = sqlite3.connect("database.db")
c = con.cursor()

c.execute("DELETE FROM names WHERE age=22")
con.commit()
con.close()



##import sqlite3
##con = sqlite3.connect("database.db")
##c = con.cursor()
##c.execute("DROP TABLE IF EXISTS names;")
##con.close()
##                                          #to delete the wholl table
