from time import sleep
import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
cursor.execute("DROP DATABASE IF EXISTS names_values;")
cursor.execute("CREATE DATABASE IF NOT EXISTS names_values DEFAULT CHARSET UTF8 ;")
database.select_db('names_values')
cursor.execute("DROP TABLE IF EXISTS names_values1")
sql1 = """CREATE TABLE IF NOT EXISTS names_values1 ( 
    Id INT(255) NOT NULL AUTO_INCREMENT,
    NAME VARCHAR(255) NOT NULL ,
    The_value INT(255) NOT NULL ,
    Name_Letter INT(255) NOT NULL ,
    Spaces INT(255) NOT NULL ,
    Modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Id)
    )"""
dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
              'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
              'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22,
              'w':23, 'x':24, 'y':25, 'z':26}
print 'any time if you want to exit the program just press "."'
print
file = open("name.txt", "w")
f = open("n.txt", "w")
while True :
    n = raw_input("Enter your name : ")
    if n == ".":
        print 'the program has stoped!'
        sleep(2)
        exit()
    n2 = n.lower()
    b = 0
    c = 0
    for char in n2 :
        if char == " ":
            continue
        c += dictionary[char]
    for x in n2 :
        if x == " ":
            b += 1
            continue
    print b
    print c
    s = len(n2)-b
    file = open("name.txt", "a")
    file.write(n2)
    file.write("\n")
    file.write(str(b))
    file.write("\n")
    file.write(str(c))
    file.write("\n")
    file.write(str(s))
    file.write("\n")
    f = open("n.txt", "a")
    for item in n2:
        f.write("%s \n"%item)
    f.write(str(b))
    f.write("\n")
    f.write(str(c))
    f.write("\n")
    f.write(str(s))
    f.write("\n")
    sql2 = "INSERT INTO `names_values1` (`Name`, `The_value`, `Name_letter`, `Spaces`) \
                VALUES(%r, %r, %r, %r);" % (n2, c, s, b)
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        database.commit()
    except:
        database.rollback()
    print s
    print n2
    print 'The lenght of spaces is ', b, 'character.'
    print 'The summition of ' , n2, ' is ', c
    print 'The length of ' , n2, ' is ', s, 'letter without spaces.'
    print
    file.close()
    f.close()
database.close()
