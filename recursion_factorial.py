def fact(n):
  return 1 if n == 1 else n * fact(n - 1)
print(fact(5))


def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)
print(factorial(5))


def factorial_for_loop(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result
print(factorial_for_loop(5))


def factorial_while_loop(n):
  result = 1
  while n > 0:
    result *= n
    n -= 1
  return result
print(factorial_while_loop(5))


def factorial_variable(n):
  if n == 0:
    return 1
  for i in range(1, n):
    n *= i
  return n
print(factorial_variable(5))


print('*' * 50)

def sum_with_previous_numbers(n):
  if n == 0 :
    return 0
  return n + sum_with_previous_numbers(n - 1)
print(sum_with_previous_numbers(5))


def sum_with_previous_odd_numbers(n):
  total = 0
  for i in range(1, n + 1, 2):
    total += i
  return total
print(sum_with_previous_odd_numbers(5))


def sum_with_previous_even_numbers(n):
  total = 0
  for i in range(2, n, 2):
    total += i
  return total
print(sum_with_previous_even_numbers(5))