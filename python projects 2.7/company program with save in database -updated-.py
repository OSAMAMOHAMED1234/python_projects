import MySQLdb
database = MySQLdb.connect("localhost", "OSAMA", "OSAMA")
cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS EMPLOYEE_DATABASE")
database.select_db('EMPLOYEE_DATABASE')
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql1 = """CREATE TABLE EMPLOYEE ( 
    Company_name VARCHAR(255),
    Id INT(255) NOT NULL AUTO_INCREMENT,
    First_name VARCHAR(255) ,
    Last_name VARCHAR(255) ,
    Gender VARCHAR(7) ,
    Date_of_birth DATE ,
    Age INT(255) ,
    Salary INT(255) ,
    Height INT(255) ,
    Weight INT(255) ,
    Phone_number TEXT ,
    Department VARCHAR(255) ,
    Office_number VARCHAR(255) ,
    Address TEXT ,
    City TEXT ,
    Country TEXT ,
    E_mail TEXT ,
    Username TEXT ,
    Password TEXT , 
    Comments TEXT,
    Modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Id)
    )"""

print 'any time if you want to exit the program just press "q"'
print
from time import sleep
n = []
first_name = raw_input('Enter your first name : ')
if first_name == 'q':
    print 'the program has stoped!'
    sleep(2)
    exit()
if first_name == ' ':
    print 'the program has stoped!'
    sleep(2)
    exit()
if first_name == '':
    print 'the program has stoped!'
    sleep(2)
    exit()
last_name = raw_input('Enter your last name : ')
gender = raw_input('Enter your gender : ')
date_of_birth = raw_input('Enter your date of birth .Ex:yyyy-mm-dd: ')
age = raw_input('Enter your age : ')
salary = raw_input('Enter your salary : ')
height = raw_input('Enter your height : ')
weight = raw_input('Enter your weight : ')
phone_number = raw_input('Enter your phone number : ')
department = raw_input('Enter your department : ')
office_number = raw_input('Enter your office number : ')
address =  raw_input('Enter your address : ')
city = raw_input('Enter your city : ')
country = raw_input('Enter your country : ')
e_mail = raw_input('Enter your e_mail : ')
username = raw_input('Enter your username : ')
password = raw_input('Enter your password : ')
comments = raw_input('Enter your comments : ')
class Employee():
    employeecountt = 0
    n.append(first_name)
    n.append(last_name)
    n.append(gender)
    n.append(date_of_birth)
    n.append(age)
    n.append(salary)
    n.append(height)
    n.append(weight)
    n.append(phone_number)
    n.append(department)
    n.append(office_number)
    n.append(address)
    n.append(city)
    n.append(country)
    n.append(e_mail)
    n.append(username)
    n.append(password)
    n.append(comments)
    file = open("Emp.txt", "w")
    file.write(str(n))
    file.close()
    f = open("E.txt", "w")
    for item in n:
        f.write("%s \n"%item)
    f.close()
    sql2 = "INSERT INTO `employee` (`Company_name`, `First_name`, `Last_name`,\
           `Gender`, `date_of_birth`, `age`, `salary`, `height`, `weight`,\
            `Phone_number`, `Department`, `Office_number`, `Address`,\
            `city`, `country`, `E_mail`, `username`, `password`, `Comments`) \
            VALUES(%r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r,\
             %r, %r, %r, %r, %r, %r, %r);" \
            % ("OSAMA", first_name, last_name, gender, date_of_birth, age, \
               salary, height, weight, phone_number, department, \
               office_number, address, city, country, e_mail, \
               username, password, comments)
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        database.commit()
    except:
        database.rollback()
    # database.close()
    def __init__(self, first_name, last_name, gender, date_of_birth, \
                 age, salary, height, weight, phone_number, department,\
                 office_number, address, city, country, e_mail, username,\
                 password, comments):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.age = age
        self.salary = salary
        self.height = height
        self.weight = weight
        self.phone_number = phone_number
        self.department = department
        self.office_number = office_number
        self.address = address
        self.city = city
        self.country = country
        self.e_mail = e_mail
        self.username = username
        self.password = password
        self.comments = comments
    def displayEmployee(self):
        print
        print 'First name            : ', self.first_name,\
              "\n"'last name             : ', self.last_name,\
              "\n"'your gender is        : ', self.gender,\
              "\n"'your date of birth is : ', self.date_of_birth,\
              "\n"'your age is           : ', self.age,\
              "\n"'your salary is        : ', self.salary,\
              "\n"'your height is        : ', self.height,\
              "\n"'your weight is        : ', self.weight,\
              "\n"'your phone number is  : ', self.phone_number,\
              "\n"'your department is    : ', self.department,\
              "\n"'your office number is : ', self.office_number,\
              "\n"'your address is       : ', self.address,\
              "\n"'your city is          : ', self.city,\
              "\n"'your country is       : ', self.country,\
              "\n"'your e-mail is        : ', self.e_mail, \
              "\n"'your username is      : ', self.username,\
              "\n"'your password is      : ', self.password,\
              "\n"'your comments is      : ', self.comments
        print
    def displaycount(self):
        Employee.employeecountt += 1
        print ('Total Employee %d' % Employee.employeecountt)
    print
    print first_name, "\t", last_name, "\t", gender, "\t", date_of_birth,\
          "\t", age, "\t", salary, "\t", height, "\t", weight,\
        "\t", phone_number, "\t", department, "\t", office_number,\
        "\t", address, "\t", city, "\t", country, "\t", e_mail,\
        "\t", username, "\t", password, "\t", comments
Employee(first_name, last_name, gender, date_of_birth, age,\
         salary, height, weight, phone_number, department,\
         office_number, address, city, country, e_mail,\
         username, password, comments).displayEmployee()
Employee(first_name, last_name, gender, date_of_birth, age,\
         salary, height, weight, phone_number, department,\
         office_number, address, city, country, e_mail,\
         username, password, comments).displaycount()

print
print n
print

while True:
    first_name = raw_input('Enter your first name : ')
    if first_name == 'q':
        print 'the program has stoped!'
        sleep(2)
        exit()
    if first_name == ' ':
        print 'the program has stoped!'
        sleep(2)
        exit()
    if first_name == '':
        print 'the program has stoped!'
        sleep(2)
        exit()
    last_name = raw_input('Enter your last name : ')
    gender = raw_input('Enter your gender : ')
    date_of_birth = raw_input('Enter your date of birth .Ex:yyyy-mm-dd: ')
    age = raw_input('Enter your age : ')
    salary = raw_input('Enter your salary : ')
    height = raw_input('Enter your height : ')
    weight = raw_input('Enter your weight : ')
    phone_number = raw_input('Enter your phone number : ')
    department = raw_input('Enter your department : ')
    office_number = raw_input('Enter your office number : ')
    address = raw_input('Enter your address : ')
    city = raw_input('Enter your city : ')
    country = raw_input('Enter your country : ')
    e_mail = raw_input('Enter your e_mail : ')
    username = raw_input('Enter your username : ')
    password = raw_input('Enter your password : ')
    comments = raw_input('Enter your comments : ')
    n.append(first_name)
    n.append(last_name)
    n.append(gender)
    n.append(date_of_birth)
    n.append(age)
    n.append(salary)
    n.append(height)
    n.append(weight)
    n.append(phone_number)
    n.append(department)
    n.append(office_number)
    n.append(address)
    n.append(city)
    n.append(country)
    n.append(e_mail)
    n.append(username)
    n.append(password)
    n.append(comments)
    file = open("Emp.txt", "w")
    file.write(str(n))
    file.close()
    f = open("E.txt", "w")
    for item in n:
        f.write("%s \n"%item)
    f.close()
    sql2 = "INSERT INTO `employee` (`Company_name`, `First_name`, `Last_name`,\
               `Gender`, `date_of_birth`, `age`, `salary`, `height`, `weight`,\
                `Phone_number`, `Department`, `Office_number`, `Address`,\
                `city`, `country`, `E_mail`, `username`, `password`, `Comments`) \
                VALUES(%r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r,\
                 %r, %r, %r, %r, %r, %r, %r);" \
           % ("OSAMA", first_name, last_name, gender, date_of_birth, age, \
              salary, height, weight, phone_number, department, \
              office_number, address, city, country, e_mail, \
              username, password, comments)
    try:
        # cursor.execute(sql1)
        cursor.execute(sql2)
        database.commit()
    except:
        database.rollback()
    Employee(first_name, last_name, gender, date_of_birth, \
                 age, salary, height, weight, phone_number, department,\
                 office_number, address, city, country, e_mail, username,\
                 password, comments)
    print
    print first_name, "\t", last_name, "\t", gender, "\t", date_of_birth, \
        "\t", age, "\t", salary, "\t", height, "\t", weight, \
        "\t", phone_number, "\t", department, "\t", office_number, \
        "\t", address, "\t", city, "\t", country, "\t", e_mail, \
        "\t", username, "\t", password, "\t", comments
    Employee(first_name, last_name, gender, date_of_birth, age, \
             salary, height, weight, phone_number, department, \
             office_number, address, city, country, e_mail, \
             username, password, comments).displayEmployee()
    Employee(first_name, last_name, gender, date_of_birth, age, \
             salary, height, weight, phone_number, department, \
             office_number, address, city, country, e_mail, \
             username, password, comments).displaycount()

    print
    print n
    print
print
database.close()