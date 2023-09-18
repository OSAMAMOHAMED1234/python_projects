from time import time

def speed_test(func):
  def inner_func(*args):
    start = time()
    func(*args)
    end = time()
    print(f'{type(func).__name__.capitalize()} Running Time is: {end - start}')
  return inner_func


@speed_test
def range_print(num):
  for n in range(num):
    print(n)

range_print(20000)