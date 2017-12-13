num = 1
while num < 100 :
    x = 2
    while x <= (num / x ):
        if not (num % x ):
            print(num, "=", x, "*", num / x)
            break
        x += 1
    if (x > num / x ):
        print (num, " is prime number.")
    num += 1
print("good bye")
