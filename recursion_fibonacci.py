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



# import time
# start = time.time()
# end = time.time()
# print(f"Runtime is {end - start}")