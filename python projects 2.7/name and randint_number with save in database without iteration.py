import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
cursor.execute("DROP DATABASE IF EXISTS name_randint;")
cursor.execute("CREATE DATABASE IF NOT EXISTS name_randint DEFAULT CHARSET UTF8 ;")
database.select_db('name_randint')
cursor.execute("DROP TABLE IF EXISTS name_randint")
sql1 = """CREATE TABLE IF NOT EXISTS name_randint (
    name VARCHAR(255) NOT NULL ,
    randint_number INT(15) NOT NULL ,
    Modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(name)
    )"""
cursor.execute(sql1)
print('any time if you want to exit the program just press "q"')
from time import sleep
from random import randint
while True :
    name = (raw_input('Enter your name : ')).lower()
    number = randint(0, 10000)
    if name == 'q' :
        print('the program has stoped!')
        sleep(2)
        exit()
    if name == ' ' :
        print('the program has stoped!')
        sleep(2)
        exit()
    if name == '' :
        print('the program has stoped!')
        sleep(2)
        exit()
    class o() :
        def __init__(self, name, number):
                self.name = name
                self.number = number
        sql2 = "INSERT INTO `name_randint` (`name`, `randint_number`)\
                VALUES(%r, %r);" % (name, number)
        try:
            cursor.execute(sql2)
            database.commit()
            print name, number
        except:
            database.rollback()
            print "this name is already existed!"
            sleep(2)
            exit()
database.close()
