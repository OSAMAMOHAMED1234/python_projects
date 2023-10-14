from timeit import default_timer

fib_num = 7

start = default_timer()
def fib(n):
  return 1 if n == 1 else 0 if n == 0 else fib(n - 1) + fib(n - 2)
print(fib(fib_num))
stop = default_timer()
print(f'fibonacci fib run time: {stop - start}')


start = default_timer()
def fibonacci(num):
  if num == 0:
    return 0
  if num == 1:
    return 1
  return fibonacci(num - 1) + fibonacci(num - 2)
print(fibonacci(fib_num))
stop = default_timer()
print(f'fibonacci run time: {stop - start}')  


start = default_timer()
def fibonacci_cached(step, _cache={}):
  if step in _cache:
    return _cache[step]
  elif step > 1:
    return _cache.setdefault(step, fibonacci_cached(step - 1) + fibonacci_cached(step - 2))
  return step
print(fibonacci_cached(fib_num))
stop = default_timer()
print(f'fibonacci cached run time: {stop - start}')


start = default_timer()
def fibonacci_cached_two(step, _cache={}):
  if step in _cache:
    return _cache[step]
  if step == 0:
    return 0
  if step == 1:
    return 1
  _cache[step] = fibonacci_cached_two(step - 1, _cache) + fibonacci_cached_two(step - 2, _cache)
  return _cache[step]
print(fibonacci_cached_two(fib_num))
stop = default_timer()
print(f'fibonacci cached two run time: {stop - start}')


start = default_timer()
def fibonacci_for_list(n):
  fib_list = [0, 1]
  for num in range(2, n + 1):
    fib_list.append(fib_list[num - 1] + fib_list[num - 2])
    # print(num, fib_list[num])
  print(f'for => {fib_list}')
  return fib_list[n]
print(fibonacci_for_list(fib_num))
stop = default_timer()
print(f'fibonacci for run time: {stop - start}')


start = default_timer()
def fibonacci_for_var(n):
  num_1, num_2 = 0, 1
  fib_list = [0, 1]
  for _ in range(2, n + 1):
    next_num = num_1 + num_2
    num_1 = num_2
    num_2 = next_num
    fib_list.append(num_2)
    # print(_, num_2)
  print(f'var => {fib_list}')
  if n < 1:
    return 0
  return num_2
print(fibonacci_for_var(fib_num))
stop = default_timer()
print(f'fibonacci var run time: {stop - start}')


start = default_timer()
def fibonacci_for_var_short(n):
  num1, num2 = 0, 1
  for _ in range(n):
    num1, num2 = num2, num1 + num2
  return num1
print(fibonacci_for_var_short(fib_num))
stop = default_timer()
print(f'fibonacci var short run time: {stop - start}')


start = default_timer()
def fibonacci_while(n):
  num1, num2 = 0, 1
  counter = 0
  fib_list = [num1]
  while counter < n:
    # next_num = num1 + num2
    # num1 = num2
    # num2 = next_num
    num1, num2 = num2, num1 + num2
    fib_list.append(num1)
    counter += 1
    # print(counter, num1)
  print(f'while => {fib_list}')
  return num1
print(fibonacci_while(fib_num))
stop = default_timer()
print(f'fibonacci while run time: {stop - start}')


# import time
# start = time.time()
# end = time.time()
# print(f"Runtime is {end - start}")