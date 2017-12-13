import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA", "osama")
cursor = database.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql1 = """CREATE TABLE EMPLOYEE (
        NAME  TEXT NOT NULL,
        SALARY   INT,
        AGE INT)"""

print 'any time if you want to exit the program just press "q"'
from time import sleep
n = []
name = raw_input('Enter your name : ')
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
salary = raw_input('Enter your salary : ')
age = raw_input('Enter your age : ')
class Employee():
    employeecountt = 0
    n.append(name)
    n.append(salary)
    n.append(age)
    file = open("Emp.txt", "w")
    file.write(str(n))
    file.close()
    f = open("E.txt", "w")
    for item in n:
        f.write("%s \n"%item)
    f.close()
    sql2 = "INSERT INTO `employee` (`NAME`, `SALARY`, `AGE`) \
            VALUES(%r, %r, %r);" % (name, salary, age)
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        database.commit()
    except:
        database.rollback()
    # database.close()
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
    def displayEmployee(self):
        print
        print 'name   : ', self.name, "\n" 'salary : ', self.salary, "\n" 'age    : ', self.age
        print
    def displaycount(self):
        Employee.employeecountt += 1
        print 'Total Employee %d' % Employee.employeecountt
    print
    print name, "\t", salary, "\t", age
Employee(name, salary, age).displayEmployee()
Employee(name, salary, age).displaycount()
print
print n
print
while True:
    name = raw_input('Enter your name : ')
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
    salary = raw_input('Enter your salary : ')
    age = raw_input('Enter your age : ')
    n.append(name)
    n.append(salary)
    n.append(age)
    file = open("Emp.txt", "w")
    file.write(str(n))
    file.close()
    f = open("E.txt", "w")
    for item in n:
        f.write("%s \n"%item)
    f.close()
    sql2 = "INSERT INTO `employee` (`NAME`, `SALARY`, `AGE`) \
            VALUES(%r, %r, %r);" % (name, salary, age)
    try:
        # cursor.execute(sql1)
        cursor.execute(sql2)
        database.commit()
    except:
        database.rollback()
    Employee(name, salary, age)
    print
    print name, "\t", salary, "\t", age
    Employee(name, salary, age).displayEmployee()
    Employee(name, salary, age).displaycount()

    print
    print n
    print
database.close()