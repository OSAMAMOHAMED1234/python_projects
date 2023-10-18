x = float(input('Enter first number : '))
y = float(input('Enter second number : '))
summ = lambda x, y : x + y ; print('+ is : ', summ(x, y))
mis = lambda x, y : x- y ; print('- is : ', mis(x, y))
mul = lambda x, y : x * y ; print('x is : ', mul(x, y))
div = lambda x, y : x / y ; print('÷ is : ', div(x, y))
pwo = lambda x, y : int((x ** y)) ; print('^ is : ', pwo(x, y))
def div(x, y):
    return x/y
print(div(x,y))

def factorial(x):
    if x == 0 :
        return 1
    else :
        return x * factorial(x - 1)
print('! is : ', factorial(x))

def summ(x):
    if x == 0 :
        return 0
    else :
        return x + summ(x - 1)
print('+- is : ', summ(x))

def sum_odd(x):
    total = 0
    for i in range(1, int((x + 1)), 2):
        total += i
    return total
print('+ الأرقام الفرديه is : ', sum_odd(x))

def sum_odd(x):
    total = 0
    for i in range(2, int((x + 1)), 2):
        total += i
    return total
print('+ الأرقام الزوجيه is : ', sum_odd(x))
