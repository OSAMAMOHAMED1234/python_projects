num = int(input("Enter your stop number : "))
a = 1
while True:
    b = a ** 2
    c = a ** 3
    if b-1 >= num:
        break
    print("number is : ", a,"\t", "& his square is : ", b,"\t", "& his cube is : ", c)
    a += 1
print("Bye")

'''
num = int(input("Enter your stop number : "))
a = 0
while True:
    a += 1
    b = a ** 2
    c = a ** 3
    if b -1 >= num:
        break
    print("number is : ", a,"\t", "& his square is : ", b,"\t", "& his cube is : ", c)
print("Bye")
'''

'''
b = 1
num = int(input("Enter your stop number : "))
while b ** 2 <= num :
    print(b ** 2)
    b += 1
'''
