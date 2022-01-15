for a in range(1, 13):
    for b in range(1, 13):
        print(a, '*', b , ' = ', a * b)
    print ('***************')


def mul_table(n, i=1):
  print (f'{n} * {i} = {n * i}')
  return mul_table(n, i + 1) if i < 12 else print('*' * 15)
for i in range(1, 13):
  mul_table(i)


def times_table(limit):
  number_format = "{{:{}}}".format(len(str(limit ** 2)))
  def times_table_recursive(number, increment):
    minimum = max(increment, 1)
    if number <= minimum * limit:
      print(number_format.format(number if number > 0 else 'x'), end=' ')
      times_table_recursive(number + minimum, increment)
    elif increment < limit:
      print()
      increment += 1
      print(number_format.format(increment), end=' ')
      times_table_recursive(increment, increment)
    else:
      print()
  times_table_recursive(0, 0)
times_table(12)

'''
for x in range(1, 13):
    for i in range(1, 13):
        print(x, 'x', i, '=', i * x)
    print('_____________')
'''
