rows = 10
for row in range(rows):
  print(' ' * (rows - row - 1) + '*' * (2 * row + 1))
for row in range(rows - 2, -1, -1):
  print(' ' * (rows - row - 1) + '*' * (2 * row + 1))


# for row in range(rows):
#   for _ in range(rows - row - 1):
#     print(' ', end='')
#   for _ in range(2 * row + 1):
#     print('*', end='')
#   print()

# for row in range(rows - 2, -1, -1):
#   for _ in range(rows - row - 1):
#     print(' ', end='')
#   for _ in range(2 * row + 1):
#     print('*', end='')
#   print()