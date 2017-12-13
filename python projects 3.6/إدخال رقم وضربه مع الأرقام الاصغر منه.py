while True :
    n = int(input('Enter a number : '))
    def factorial(n):
        if n == 0 :
            return 1
        else :
            return n * factorial(n - 1)
    print(factorial(n))


while True :
    result = 1
    a = input("Enter your factorial number : ")
    if a == "":
        exit()
    elif a == " ":
        exit()
    for i in range(1,  int(a)+ 1):
        result *= i
    print("The result is : ", result)
