from timeit import default_timer

fib_num = 7

start = default_timer()
def fibonacci(num):
  if num == 0:
    return 0
  if num == 1:
    return 1
  return fibonacci(num - 1) + fibonacci(num - 2)
print(fibonacci(fib_num))

stop = default_timer()
print('fibonacci run time: ', stop - start)  


start = default_timer()
def fibonacci_cached(step, _cache={}):
  if step in _cache:
    return _cache[step]
  elif step > 1:
    return _cache.setdefault(step, fibonacci_cached(step - 1) + fibonacci_cached(step - 2))
  return step
print(fibonacci_cached(fib_num))

stop = default_timer()
print('fibonacci cached run time: ', stop - start)


def fibonacci_for_list(n):
  fib_list = [0, 1]
  for num in range(2, n + 1):
    fib_list.append(fib_list[num - 1] + fib_list[num - 2])
    # print(num, fib_list[num])
  print('for', fib_list)
  return fib_list[n]
print(fibonacci_for_list(fib_num))


def fibonacci_for_var(n):
  num_1, num_2 = 0, 1
  fib_list = [0, 1]
  for _ in range(2, n + 1):
    next_num = num_1 + num_2
    num_1 = num_2
    num_2 = next_num
    fib_list.append(num_2)
    # print(_, num_2)
  print('var', fib_list)
  if n < 1:
    return 0
  return num_2
print(fibonacci_for_var(fib_num))


def fibonacci_while(n):
  num_1, num_2 = 0, 1
  counter = 0
  fib_list = [num_1]
  while counter < n:
    next_num = num_1 + num_2
    num_1 = num_2
    num_2 = next_num
    fib_list.append(num_1)
    counter += 1
    # print(counter, num_1)
  print('while', fib_list)
  return num_1
print(fibonacci_while(fib_num))


# import time
# start = time.time()
# end = time.time()
# print(f"Runtime is {end - start}")