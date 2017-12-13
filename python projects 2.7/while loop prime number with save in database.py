import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
cursor.execute("DROP DATABASE IF EXISTS prime_p;")
cursor.execute("CREATE DATABASE IF NOT EXISTS prime_p DEFAULT CHARSET UTF8 ;")
database.select_db('prime_p')
cursor.execute("DROP TABLE IF EXISTS prime_table")
sql1 = """CREATE TABLE IF NOT EXISTS prime_table (
    RESULT INT(3) NOT NULL ,
    equal VARCHAR(1) NOT NULL ,
    first_number VARCHAR(15) NOT NULL ,
    multiply VARCHAR(1) NOT NULL ,
    second_number VARCHAR(2) NOT NULL ,  
    Modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(RESULT)
    )"""
cursor.execute(sql1)
num = 1
while num < 100 :
    x = 2
    while x <= (num / x ):
        if not (num % x ):
            sql2 = "INSERT INTO `prime_table` (`RESULT`, `equal`, `first_number`, `multiply`, `second_number`)\
                    VALUES(%r, %r, %r, %r, %r);" % (num , "=", x, "*", num / x)
            cursor.execute(sql2)
            print num, "=", x, "*", num / x
            break
        x += 1
    if (x > num / x ):
        sql3 = "INSERT INTO `prime_table` (`RESULT`, `equal`, `first_number`, `multiply`, `second_number`)\
                VALUES(%r, %r, %r, %r, %r);" % (num, " ", "is prime number", " ", " ")
        cursor.execute(sql3)
        print num, " is prime number."
    num += 1
try:
    database.commit()
except:
    database.rollback()
database.close()
