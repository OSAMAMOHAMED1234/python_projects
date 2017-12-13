dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
              'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
              'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22,
              'w':23, 'x':24, 'y':25, 'z':26}
l = ["1","2","3","4","5","6","7","8","9","0"]
n = input("Enter your name : ")
n2 = n.lower()
space = 0
value = 0
numbers = 0
number = []
summ = 0
letter = []
for char in n2 :
    if char == " ":
        space += 1
        continue
    elif char in l :
        numbers += 1
        n = number.append(char)
        continue
    value += dictionary[char]
    letter.append(char)
print()
for let in letter:
    print('The value of ', let, ' is : ', dictionary[let])
print()
for let in letter:
    print(let, end='')
print()
for item in number:
    summ += int(item)
    print(item, end='')
print()
print()
print(value)
print(summ)
print(space)
print(numbers)
print(((len(n2)) - (space) - (numbers)))
print(len(n2)- space)
print(len(n2))
print((n2[::-1]))
print()
print('The value of ', n2, 'is :', value)
print('The summation of number(s) in ', n2, 'is :', summ)
print('The lenght of space(s) is :', space, 'space(s)')
print('The lenght of number(s) is :', numbers, 'number(s)')
print('The length of letter(s) is :', len(n2) - space - numbers, 'letter(s)')
print('The whole length of ' , n2, ' is :', len(n2)- space, 'letter(s) & number(s)')
print('The whole length of ' , n2, ' is :', len(n2), 'letter(s) & number(s) with space(s)')
print('The word(s) reverse is : ', n2[::-1])
print()
print('---------------------------------------------------------------------------------')
print()

#
for let in letter:
    print('The value of ', let, ' is : ', dictionary[let])
print()
#

#
for let in letter:
    print(let, end='')
print()
#

#
for item in number:
    #summ += int(item)
    print(item, end='')
print()
print()
#

#
print(value)
print(summ)
print(space)
print(numbers)
print(((len(n2)) - (space) - (numbers)))
print(len(n2)- space)
print(len(n2))
#

#
rr = number[::-1]
for num in rr:
    print(num, end='')
r = letter[::-1]
for let in r:
    print(let, end='')
print()
print()
#

#
print('The value of ', end='')
for let in letter:
    print(let, end='')
print(' is :', value)
#

#
print('The summation of ', end='')
for num in number:
    print(num, end='')
print(' is :', summ)
#

#
print('The lenght of space(s) is :', space, 'space(s)')
print('The lenght of number(s) is :', numbers, 'number(s)')
print('The length of letter(s) is :', len(n2) - space - numbers, 'letter(s)')
#

#
print('The whole length of ', end='')
for let in letter:
    print(let, end='')
for num in number:
    print(num, end='')
print(' is :', len(n2)- space, 'letter(s) & number(s)')
#

#
print('The whole length of ', end='')
for let in letter:
    print(let, end='')
for num in number:
    print(num, end='')
print(' is :', len(n2), 'letter(s) & number(s) with space(s)')
#

#
print('The word(s) reverse is : ', end='')
rr = number[::-1]
for num in rr:
    print(num, end='')
r = letter[::-1]
for let in r:
    print(let, end='')
print()
print()
print('good bye!')
print()
#
