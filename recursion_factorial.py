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

