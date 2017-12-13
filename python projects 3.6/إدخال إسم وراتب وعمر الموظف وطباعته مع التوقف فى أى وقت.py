print('any time if you want to exit the program just press "q"')
from random import randint
from time import sleep
n = []
while True :
    name = input('Enter your name : ')
    if name == 'q' :
        print('the program has stoped!')
        sleep(2)
        break
    if name == ' ' :
        print('the program has stoped!')
        sleep(2)
        break
    if name == '' :
        print('the program has stoped!')
        sleep(2)
        break
    salary = input('Enter your salary : ')
    age = input('Enter your age : ')
    class Employee() :
        employeecountt = 0
        n.append(name)
        n.append(salary)
        n.append(age)
        def __init__(self, name, salary, age):
            self.name = name
            self.salary = salary
            self.age = age
            Employee.employeecountt +=1
        def displayEmployee(self):
            print()
            print('name   : ', self.name,"\n" 'salary : ', self.salary,"\n" 'age    : ', self.age)
            print()
        def displaycount(self):
            print('Total Employee %d'% Employee.employeecountt)
        print()    
        print(name,"\t", salary,"\t", age)
            
    Employee(name, salary, age).displayEmployee()
    #e1 = Employee(name, salary)
    #e1.displayEmployee()
    Employee(name, salary, age).displaycount()
    
    print()
    print(n)
    print()
