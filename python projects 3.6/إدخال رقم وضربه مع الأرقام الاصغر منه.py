def factorial_iter(n):
  result = 1
  for n in range(1, n + 1):
    result *= n
  return result
print(factorial_iter(5))

def fact(n):
  return 1 if n == 1 else n * fact(n - 1)
print(fact(5))


while True :
  n = int(input('Enter a number : '))
  def factorial(n):
    if n == 0 :
      return 1
    else :
      return n * factorial(n - 1)
  print(factorial(n))


while True :
  result = 1
  a = input("Enter your factorial number : ")
  if a == "":
    exit()
  elif a == " ":
    exit()
  for i in range(1,  int(a)+ 1):
    result *= i
  print("The result is : ", result)
