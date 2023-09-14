def check_leap(year):  
  if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):      
    return f"{year} is a leap Year"
  else:  
    return f"{year} is not a leap Year"

for x in range(1990, 2050):
  print(check_leap(x))