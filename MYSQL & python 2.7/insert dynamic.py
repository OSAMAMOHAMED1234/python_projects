import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA", "osama")
cursor = database.cursor()
sql = "INSERT INTO EMPLOYEE (\
        FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)\
        VALUES ('%s', '%s', '%d', '%c', '%d')"%\
        ("OSAMA", "MOHAMED", 22, "M", 6000)
try:
    cursor.execute(sql)
    database.commit()
except:
    database.rollback()
database.close()