# solid
for i in range(6):
  for j in range(i + 1):
    print('*', end=' ')
  print()


print('=' * 50)

# hollow
for r in range(6):
  for c in range(r):
    print (' ', end=' ')
  print('*')