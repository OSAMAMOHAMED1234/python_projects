def leap_years(start_year, end_year):
  leap_years = []
  for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      leap_years.append(year)
  return leap_years
print(leap_years(2000, 2030))


def is_leap_year(year):
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def print_leap_years(start_year, end_year):
  for year in range(start_year, end_year + 1):
    if is_leap_year(year):
      print(year)
print_leap_years(2000, 2030)