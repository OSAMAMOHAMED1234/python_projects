import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
cursor.execute("DROP DATABASE IF EXISTS number;")
cursor.execute("CREATE DATABASE IF NOT EXISTS number DEFAULT CHARSET UTF8 ;")
database.select_db('number')
cursor.execute("DROP TABLE IF EXISTS number_square_cube")
sql1 = """CREATE TABLE IF NOT EXISTS number_square_cube (
    number INT(10) NOT NULL ,
    square INT(20) NOT NULL ,
    cube INT(20) NOT NULL ,
    Modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(number)
    )"""
cursor.execute(sql1)
x = int(raw_input('Enter th starting number : '))
y = int(raw_input('Enter the stop number : '))
print
print 'Number \t square', '', 'cube'
print '----------------------'
for a in range(x, y+1):
    sql2 = "INSERT INTO `number_square_cube` (`number`, `square`, `cube`)\
            VALUES(%r, %r, %r);" % (a , a**2, a**3)
    cursor.execute(sql2)
    print a, '\t', a**2, '\t', a**3
try:
    database.commit()
except:
    database.rollback()
database.close()
