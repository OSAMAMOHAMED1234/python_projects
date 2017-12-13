import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA", "osama")
cursor = database.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
        FIRST_NAME  CHAR(20) NOT NULL,
        LAST_NAME   CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT )"""
cursor.execute(sql)
database.close()