import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
cursor.execute("DROP DATABASE IF EXISTS numbers;")
cursor.execute("CREATE DATABASE IF NOT EXISTS numbers DEFAULT CHARSET UTF8 ;")
database.select_db('numbers')
cursor.execute("DROP TABLE IF EXISTS numbers")
sql1 = """CREATE TABLE IF NOT EXISTS numbers (
    first_number INT(15) NOT NULL ,
    second_number INT(15) NOT NULL ,
    third_number INT(15) NOT NULL ,
    result INT(15) NOT NULL,
    Modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )"""
cursor.execute(sql1)
a  = int(raw_input('Enter the first number : '))
a2 = int(raw_input('Enter the second number : '))
a3 = int(raw_input('Enter the third number : '))
for x in range(10):
    for y in range(10):
        for z in range(10):
            s = x + y + z
            sql2 = "INSERT INTO `numbers` (`first_number`, `second_number`, `third_number`, `result`)\
                    VALUES(%r, %r, %r, %r);" % (x , y, z, s)
            cursor.execute(sql2)
            print x, y, z
            if (x == a and y == a2 and z == a3):
                break
        else :
            continue
        break
    else :
        continue
    break
try:
    database.commit()
except:
    database.rollback()
database.close()
