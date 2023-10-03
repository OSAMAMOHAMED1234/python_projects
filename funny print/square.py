rows = 6
# solid
for i in range(rows):
  for j in range(rows):
    print('*', end='')
  print()

print('*' * 50)

# hollow
for i in range(rows):
  for j in range(rows):
    if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
      print('*', end='')
    else:
      print(' ', end='')
  print()