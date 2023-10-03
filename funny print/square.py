rows = 6
# solid
for i in range(rows):
  for j in range(rows):
    print('*', end='')
  print()

print('*' * 50)

# hollow
for row in range(rows):
  for col in range(rows):
    if row == 0 or row == rows - 1 or col == 0 or col == rows - 1:
      print('*', end='')
    else:
      print(' ', end='')
  print()