x = int(input('Enter th starting number : '))
y = int(input('Enter the stop number : '))
print()
print('Number \t square', '', 'cube')
print('----------------------')
for a in range(x, y+1):
    print (a, '\t', a**2, '\t', a**3)
