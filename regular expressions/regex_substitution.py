import re


n = int(input())
for line in range(n):
  string = input()
  replace_and = re.sub('(?<= )(&&)(?= )', 'and', string)
  replace_or = re.sub('(?<= )(\|\|)(?= )', 'or', replace_and)
  print(replace_or)