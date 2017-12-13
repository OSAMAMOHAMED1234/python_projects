print 'any time if you want to exit the program just press "q"'
from time import sleep
import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
#cursor.execute("DROP DATABASE IF EXISTS names_passwords;")
cursor.execute("CREATE DATABASE IF NOT EXISTS names_passwords DEFAULT CHARSET UTF8 ;")
database.select_db('names_passwords')
#cursor.execute("DROP TABLE IF EXISTS `name`")
cursor.execute("""CREATE TABLE IF NOT EXISTS `name` ( 
    Id INT(255) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    User_Name VARCHAR(255) NOT NULL ,
    pass_word INT(255) NOT NULL ,
    mail VARCHAR(255) NOT NULL ,
    Modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
    """)
while True:
    database = MySQLdb.connect("localhost", "OSAMA", "OSAMA", "names_passwords")
    cursor = database.cursor()
    cursor.execute("SELECT User_Name FROM name;")
    names = []
    results = cursor.fetchall()
    for row in results :
        res = row[0]
        nn = names.append(res)
    print "user's names is : %s " % (names)
    name = raw_input("Enter your user name : ").lower()
    if name == 'q':
        print 'the program has stoped!'
        sleep(2)
        exit()
    if name == ' ':
        print 'the program has stoped!'
        sleep(2)
        exit()
    if name == '':
        print 'the program has stoped!'
        sleep(2)
        exit()
    if name not in names:
        pa   = raw_input("Enter your password : ").lower()
        mail = raw_input("Enter your e-mail : ").lower()
        sql2 = "INSERT INTO `name`(`User_Name`, `pass_word`, `mail`) \
                VALUES(%r, %r, %r);" % (name, pa, mail)
        print "You are registered now!"
        try:
            cursor.execute(sql2)
            database.commit()
        except:
            database.rollback()
    else:
        print "You have already registered!"
        sleep(2)
        exit()
database.close()
