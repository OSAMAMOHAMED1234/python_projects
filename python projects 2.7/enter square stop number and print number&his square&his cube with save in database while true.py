import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
cursor.execute("DROP DATABASE IF EXISTS number_s_c;")
cursor.execute("CREATE DATABASE IF NOT EXISTS number_s_c DEFAULT CHARSET UTF8 ;")
database.select_db('number_s_c')
cursor.execute("DROP TABLE IF EXISTS number")
sql1 = """CREATE TABLE IF NOT EXISTS number (
    number_is VARCHAR(12) NOT NULL,
    number INT(12) NOT NULL ,
    his_square VARCHAR(18) NOT NULL,
    square_number INT(12) NOT NULL ,
    his_cube VARCHAR(16) NOT NULL,
    cube_number INT(12) NOT NULL ,
    Modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )"""
cursor.execute(sql1)
num = int(input("Enter your stop number : "))
a = 0
while True:
    a += 1
    b = a ** 2
    c = a ** 3
    if b >= num:
        break
    print "number is : ", a,"\t", "& his square is : ", b,"\t", "& his cube is : ", c
    sql2 = "INSERT INTO `number` (`number_is`, `number`, `his_square`, `square_number`, `his_cube`, `cube_number`)\
                VALUES(%r, %r, %r, %r, %r, %r);" % ("number is : ", a, "& his square is : ", b, "& his cube is : ", c)
    cursor.execute(sql2)
print "Bye"
try:
    database.commit()
except:
    database.rollback()
database.close()
