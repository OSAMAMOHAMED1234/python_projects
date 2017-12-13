syear = int(input("Enter the start number of yaer : "))
eyear = int(input("Enter the end number of yaer : "))
for a1 in range(syear, eyear+1):
    for a2 in range(1, 13):
        for a3 in range(1, 13):
            if a2 == a3 :
                print(a1, "-", a2, "-", a3)


##for a1 in range(2000, 2021):
##    for a2 in range(1, 13):
##        for a3 in range(1, 13):
##            if a2 == a3 :
##                print(a1, "-", a2, "-", a3)
