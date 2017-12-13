import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA", "osama")
cursor = database.cursor()
sql = "UPDATE EMPLOYEE SET AGE = AGE +2 WHERE 1"
try:
    cursor.execute(sql)
    database.commit()
except:
    database.rollback()
database.close()
