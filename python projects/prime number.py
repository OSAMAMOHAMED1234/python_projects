num1, num2 = int(1), int(100)

for number in range(num1, num2 + 1):
  if number == 1:
    continue
  for x in range(2, number):
    if number % x == 0:
      print(number, '=', x, '*', int(number/x))
      break
  else:
    print(number, 'is prime number')


print('=' * 36)

for number in range(num1, num2 + 1):
  for x in range(2, num2 + 1):
    if number == x:
      print(number, 'is prime number')
      continue
    if number % x == 0 :
      print(number, '=', x, '*', int(number / x))
      break


print('=' * 36)

number1, number2 = int(1), int(100)
while number1 <= number2:
  x = 2
  while x < number2:
    if number1 == x:
      print(number1, 'is prime number')
      break
    if number1 % x == 0:
      print(number1, '=', x, '*', int(number1 / x))
      break
    x += 1
  number1 += 1


print('=' * 36)

def prime_number(number):
  for i in range(2, 1 + number // 2):
    if number % i == 0:
      return False, number, i
  return True, number

for n in range(num1, num2 + 1):
  if n == 1:
    continue
  if prime_number(n)[0] == True:
    print(n, 'is prime number')
  else:
    print(n, '=', prime_number(n)[2], '*', int(n/prime_number(n)[2]))


# num = 1
# while num < 100 :
#     x = 2
#     while x <= (num / x ):
#         if not (num % x ):
#             print(num, "=", x, "*", num / x)
#             break
#         x += 1
#     if (x > num / x ):
#         print (num, " is prime number.")
#     num += 1
# print("good bye")
