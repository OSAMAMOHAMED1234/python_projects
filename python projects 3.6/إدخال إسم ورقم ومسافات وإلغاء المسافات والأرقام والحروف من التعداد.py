n = input("Enter your name : ")
n2 = n.lower()
b = 0
c = 0
l = ["1","2","3","4","5","6","7","8","9","0"]
for x in n2 :
    if x == " ":
        b += 1
        continue
    elif x in l :
        c += 1
        continue

print(b)
print(c)
print(len(n2) - b - c)
print(len(n2)-b)
print(len(n2))
print('The lenght of spaces is ', b, 'space(s)')
print('The lenght of numbers is ', c, 'number(s)')
print('The length of letters is ', len(n2) - b - c, 'letter(s)')
print('The whole length of ' , n2, ' is ', len(n2)-b, 'letter(s) & number(s)')
print('The whole length of ' , n2, ' is ', len(n2), 'letter(s) & number(s) with space(s)')
