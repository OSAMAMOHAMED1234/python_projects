print('any time if you want to exit the program just press "q"')
#import time
from time import sleep
from random import randint
while True :
    name = input('Enter your name : ')
    number = randint(0, 10000)
    if name == 'q' :
        print('the program has stoped!')
        #time.sleep(2)
        sleep(2)
        break
    if name == ' ' :
        print('the program has stoped!')
        #time.sleep(2)
        sleep(2)
        break
    if name == '' :
        print('the program has stoped!')
        #time.sleep(2)
        sleep(2)
        break
    class o() :
        #number = randint(0, 10000)
        def __init__(self, name, number):
                self.name = name
                self.number = number
                
        print(name, number)
