a  = int(input('Enter the first number : '))
a2 = int(input('Enter the second number : '))
a3 = int(input('Enter the third number : '))
for x in range(10):
    for y in range(10):
        for z in range(10):
            print(x, y, z)
            if (x == a and y == a2 and z == a3):
                break
        else :
            continue
        break
    else :
        continue
    break
