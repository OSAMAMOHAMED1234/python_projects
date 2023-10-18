string = input()
print(''.join(sorted(string, key=lambda x: (
  x.isdigit() and int(x) % 2 == 0, x.isdigit(), x.isupper(), x.islower(), x))))


def order_function(x):
  if x.islower():
    return (1, x)
  elif x.isupper():
    return (2, x)
  else:
    return (3 if int(x) % 2 == 1 else 4, x)
print(*sorted(string, key=order_function), sep='')