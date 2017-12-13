for number in range(1, 100):
    for x in range(2, number):
        if number % x == 0:
            #v = number / x
            #print ('%d = %d * %d' % (number, x, v))
            print (number, '=', x, '*', int(number/x))
            break
    else:
        print(number, 'is prime number')
