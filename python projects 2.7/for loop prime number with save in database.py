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
for number in range(1, 100):
    for x in range(2, number):
        if number % x == 0:
            z = int(number/x)
            sql2 = "INSERT INTO `prime_table` (`RESULT`, `equal`, `first_number`, `multiply`, `second_number`)\
                VALUES(%r, %r, %r, %r, %r);" % (number , "=", x, "*", z)
            cursor.execute(sql2)
            print (number, '=', x, '*', z)
            break
    else:
        sql3 = "INSERT INTO `prime_table` (`RESULT`, `equal`, `first_number`, `multiply`, `second_number`)\
                VALUES(%r, %r, %r, %r, %r);" % (number, " ", "is prime number", " ", " ")
        cursor.execute(sql3)
        print(number, 'is prime number')
try:
    database.commit()
except:
    database.rollback()
database.close()
