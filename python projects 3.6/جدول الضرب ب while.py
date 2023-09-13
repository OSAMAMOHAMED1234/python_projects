table1, table2, t1 = 12, 12, 0
while t1 < table1:
    t1 += 1
    t2 = 0
    while t2 < table2:
        t2 += 1
        print(f'{t1} * {t2} = {t1 * t2}')
    print('=' * 50)



a = 0
b = 0
while a < 12 :
    a += 1
    b  = 0
    print()
    print ('**************')
    print()
    while b < 12:
        b += 1
        print(a, '*', b , ' = ', a * b)
