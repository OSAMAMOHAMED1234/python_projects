from time import sleep
import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
cursor.execute("DROP DATABASE IF EXISTS names_passwords;")
cursor.execute("CREATE DATABASE IF NOT EXISTS names_passwords DEFAULT CHARSET UTF8 ;")
database.select_db('names_passwords')
cursor.execute("DROP TABLE IF EXISTS `name`")
sql1 = """CREATE TABLE IF NOT EXISTS `name` ( 
    /*Id INT(255) NOT NULL UNIQUE AUTO_INCREMENT ,*/
    User_Name VARCHAR(255) NOT NULL PRIMARY KEY,
    pass_word INT(255) NOT NULL ,
    mail VARCHAR(255) NOT NULL ,
    Modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
    """
while True :
    name = raw_input("Enter your user name : ").lower()
    if name == ' ':
        print 'the program has stoped!'
        sleep(2)
        exit()
    if name == '':
        print 'the program has stoped!'
        sleep(2)
        exit()
    pa   = raw_input("Enter your password : ").lower()
    mail = raw_input("Enter your e-mail : ").lower()
    sql2 = "INSERT INTO `name`(`User_Name`, `pass_word`, `mail`) \
            VALUES(%r, %r, %r);" % (name, pa, mail)
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        print "You are registered now!"
        database.commit()
    except:
        #cursor.execute("DELETE FROM `name` WHERE `Id` = 0;")
        database.rollback()
        print "You have already registered!"
        sleep(2)
        exit()
    database = MySQLdb.connect("localhost", "OSAMA", "OSAMA", "names_passwords")
    cursor = database.cursor()
    sql = "SELECT User_Name, pass_word, mail FROM name;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results :
            User_Name = row[0]
            pass_word = row[1]
            mail = row[2]
            print "User Name = %s , password = %d , mail = %s"\
            % (User_Name, pass_word, mail)
    except:
        print "Error : unable to fecth data"
database.close()
