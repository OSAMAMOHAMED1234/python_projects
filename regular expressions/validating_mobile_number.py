from re import compile, match

n = int(input())
for _ in range(n):
  mobile_number = input()
  condition = compile(r'^0\d{10}$')
  if bool(match(condition, mobile_number)):
    print('YES')
  else:
    print('NO')