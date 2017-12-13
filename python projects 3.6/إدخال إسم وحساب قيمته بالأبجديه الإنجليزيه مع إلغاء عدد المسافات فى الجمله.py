dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
              'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
              'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22,
              'w':23, 'x':24, 'y':25, 'z':26}
n = input("Enter your name : ")
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
print(b)
print(c)
print(len(n2)-b)
print(n2)
print('The lenght of spaces is ', b, 'character.')
print('The summition of ' , n2, ' is ', c)
print('The length of ' , n2, ' is ', len(n2)-b, 'letter without spaces.')


'''
dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
              'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
              'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22,
              'w':23, 'x':24, 'y':25, 'z':26}
from time import sleep
print('any time if you want to exit the program just press "."')
print()
while True :
    n = input("Enter your name : ")
    if n == ".":
        print('the program has stoped!')
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
    print(b)
    print(c)
    print(len(n2)-b)
    print(n2)
    print('The lenght of spaces is ', b, 'character.')
    print('The summition of ' , n2, ' is ', c)
    print('The length of ' , n2, ' is ', len(n2)-b, 'letter without spaces.')
    print()
'''
