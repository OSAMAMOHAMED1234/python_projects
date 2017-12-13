import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA", "osama")
cursor = database.cursor()
sql = "DELETE FROM EMPLOYEE WHERE AGE = 22 "
try:
    cursor.execute(sql)
    database.commit()
except:
    database.rollback()
database.close()