print('any time if you want to exit the program just press "q"')
from time import sleep
n = []
name = input('Enter your name : ')
if name == 'q':
    print('the program has stoped!')
    sleep(2)
    exit()
if name == ' ':
    print('the program has stoped!')
    sleep(2)
    exit()
if name == '':
    print('the program has stoped!')
    sleep(2)
    exit()
salary = input('Enter your salary : ')
age = input('Enter your age : ')
# n.append(name)
# n.append(salary)
# n.append(age)
class Employee():
    employeecountt = 0
    n.append(name)
    n.append(salary)
    n.append(age)
    file = open("Emp.txt", "w")
    file.write(str(n))
    file.close()
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
    def displayEmployee(self):
        print()
        print('name   : ', self.name, "\n" 'salary : ', self.salary, "\n" 'age    : ', self.age)
        print()
    def displaycount(self):
        Employee.employeecountt += 1
        print('Total Employee %d' % Employee.employeecountt)
    print()
    print(name, "\t", salary, "\t", age)
Employee(name, salary, age).displayEmployee()
    # e1 = Employee(name, salary)
    # e1.displayEmployee()
Employee(name, salary, age).displaycount()
print()
print(n)
print()
while True:
    name = input('Enter your name : ')
    if name == 'q':
        print('the program has stoped!')
        sleep(2)
        exit()
    if name == ' ':
        print('the program has stoped!')
        sleep(2)
        exit()
    if name == '':
        print('the program has stoped!')
        sleep(2)
        exit()
    salary = input('Enter your salary : ')
    age = input('Enter your age : ')
    n.append(name)
    n.append(salary)
    n.append(age)
    file = open("Emp.txt", "w")
    file.write(str(n))
    file.close()
    Employee(name, salary, age)
    print()
    print(name, "\t", salary, "\t", age)
    Employee(name, salary, age).displayEmployee()
        # e1 = Employee(name, salary)
        # e1.displayEmployee()
    Employee(name, salary, age).displaycount()

    print()
    print(n)
    print()
