import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA", "osama")
cursor = database.cursor()
sql = "SELECT * FROM EMPLOYEE \
       WHERE 1"
''' AGE > '%d'" % (20) '''
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results :
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print "first name = %s , last name = %s , age = %d , sex = %s , income = %d "\
        % (fname, lname, age, sex, income)
except:
    print "Error : unable to fecth data"
database.close()