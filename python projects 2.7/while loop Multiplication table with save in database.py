import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
cursor.execute("DROP DATABASE IF EXISTS multiply_s;")
cursor.execute("CREATE DATABASE IF NOT EXISTS multiply_s DEFAULT CHARSET UTF8 ;")
database.select_db('multiply_s')
cursor.execute("DROP TABLE IF EXISTS multiply_table")
sql1 = """CREATE TABLE IF NOT EXISTS multiply_table (
    first_number INT(2) NOT NULL ,
    multiply VARCHAR(1) NOT NULL ,
    second_number INT(2) NOT NULL ,
    equal VARCHAR(1) NOT NULL ,
    RESULT INT(3) NOT NULL ,
    Modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )"""
cursor.execute(sql1)
a = 0
b = 0
while a < 12 :
    a += 1
    b  = 0
    while b < 12:
        b += 1
        c = a * b
        print a, '*', b , ' = ', c
        sql2 = "INSERT INTO `multiply_table` (`first_number`, `multiply`, `second_number`, `equal`, `RESULT`)\
                VALUES(%r, %r, %r, %r, %r);" % (a, "*", b, "=", c)
        cursor.execute(sql2)
    print '**************'
try:
    database.commit()
except:
    database.rollback()
database.close()
