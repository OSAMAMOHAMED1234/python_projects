print('any time if you want to exit the program just press "q"')
print()
while True:
    a = (input("Enter the number of month -or- the name of month : ").lower())
    from time import sleep
    if a == 'q':
        print('the program has stoped!')
        sleep(2)
        exit()
    if a == ' ':
        print('the program has stoped!')
        sleep(2)
        exit()
    if a == '':
        print('the program has stoped!')
        sleep(2)
        exit()
    if a == "2" or a == "february":
        print(28, "days in this month")
        print() 
    elif    a == "4" or a == "april" \
         or a == "6" or a == "june" \
         or a == "9" or a == "september" \
         or a == "11" or a == "november":
        print(30, "days in this month")
        print()
        
    elif    a == "1" or a == "january" \
         or a == "3" or a == "march" \
         or a == "5" or a == "may" \
         or a == "7" or a == "july" \
         or a == "8" or a == "august" \
         or a == "10" or a == "october" \
         or a == "12" or a == "december":
        print(31, "days in this month")
        print()
    else:
        print("You have typed incorrectly , please try again!")
        print()
