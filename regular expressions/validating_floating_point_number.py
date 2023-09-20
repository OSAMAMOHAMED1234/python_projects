import re
pattern = r'^[-+]?[0-9]{,}[.][0-9]{1,}$'

for _ in range(int(input())):
  print(True if re.search(pattern, input()) else False)