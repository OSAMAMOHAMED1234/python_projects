n = input("Enter your name : ")
n2 = n.lower()
b = 0
for x in n2 :
    if x == " ":
        b += 1
        continue
print(b)
print(len(n2)-b)
print('The lenght of spaces is ', b, 'letter')
print('The length of ' , n2, ' is ', len(n2)-b, 'letter')
