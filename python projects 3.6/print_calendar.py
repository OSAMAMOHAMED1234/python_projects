import calendar
print(calendar.TextCalendar(firstweekday=5).formatyear(2023))
print(calendar.TextCalendar(firstweekday=5).formatmonth(theyear=2023, themonth=10))

print(calendar.day_name[calendar.weekday(2023, 9, 18)].upper())
print(calendar.month_name[10].upper())

for i in range(1, 13):
  print(f'Month short name is: {calendar.month_abbr[i]}, Full name is: {calendar.month_name[i]}')

for i in range(1, 7):
  print(f'Day short name is: {calendar.day_abbr[i]}, Full name is: {calendar.day_name[i]}')