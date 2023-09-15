def print_door_mat(num1, num2):
  res = []
  for i in range(num1//2):
    res.append(('.|.' * (2 * i + 1)).center(num2, '-'))
  return print('\n'.join(res + ['WELCOME'.center(num2, '-')] + res[::-1]))

print_door_mat(7, 21)
# num1, num2 = map(int,input().split())
# print_door_mat(num1, num2)