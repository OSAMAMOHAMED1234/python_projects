from infix_postfix import infix_to_postfix

def infix_to_prefix(expression):
  reverse_expr = ''
  for i in expression[::-1]:
    if i == '(':
      reverse_expr += ')'
    elif i == ')':
      reverse_expr += '('
    else:
      reverse_expr += i
  return infix_to_postfix(reverse_expr)[::-1]
print(infix_to_prefix('A+B*C+D'))


def evaluate_prefix(expression):
  stack = []
  for i in expression[::-1]:
    if i.isdigit():
      stack.append(int(i))
    else:
      val1 = stack.pop()
      val2 = stack.pop()
      if i == '+':
        stack.append(val1 + val2)
      elif i == '-':
        stack.append(val1 - val2)
      elif i == '*':
        stack.append(val1 * val2)
      elif i == '/':
        stack.append(val1 / val2)
  return int(stack.pop())
 
print(evaluate_prefix('-+8/632')) # 8
print(evaluate_prefix('-+7*45+20')) # 25
print(evaluate_prefix('+9*26')) # 21
print(evaluate_prefix('-*33+2+11')) # 5
print(evaluate_prefix('-+5*+1243')) # 14
print(evaluate_prefix('*+35-72')) # 40
print(evaluate_prefix('+34')) # 7
print(evaluate_prefix('*-567')) # -7


def prefix_to_infix(prefix):
  operators, stack, i = set(['+', '-', '*', '/', '(', ')', '^', '%']), [], len(prefix) - 1
  while i >= 0:
    if prefix[i] not in operators:
      stack.append(prefix[i])
    else:
      val1 = stack.pop()
      val2 = stack.pop()
      stack.append('(' + val1 + prefix[i] + val2 + ')')
    i -= 1
  return stack.pop()
print(prefix_to_infix('*+ABC')) # ((A+B)*C)
print(prefix_to_infix('*+AB-CD')) # ((A+B)*(C-D))
print(prefix_to_infix('*-A/BC-/AKL')) # ((A-(B/C))*((A/K)-L))
print(prefix_to_infix('+*ab^cd')) # ((a*b)+(c^d))
print(prefix_to_infix('-+*^%adcex*y^ab')) # (((((a%d)^c)*e)+x)-(y*(a^b)))



# import operator
# def eval_prefix(expression):
#   d = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '%': operator.mod}
#   for n in range(10):
#     d[str(n)] = n
#   e = list(d.get(e, None) for e in expression)
#   i = 0
#   while i + 3 <= len(e):
#     o, l, r = e[i : i + 3]
#     if type(o) == type(operator.add) and type(l) == type(r) == type(0):
#       e[i : i + 3] = [o(l, r)]
#       i = 0
#     else:
#       i += 1
#   # if len(e) != 1:
#   #   print('Error in expression:', expression)
#   #   return 0
#   # else:
#   #   return e[0]
#   return print('Error in expression:', expression) if len(e) != 1 else e[0]
# print(eval_prefix('+34'))
# print(eval_prefix('*-567'))
# print(eval_prefix('-*33+2+11'))
# print(eval_prefix('-+5*+1243'))
# print(eval_prefix('*+35-72'))

# print(eval_prefix('%3/52'))
# print(eval_prefix('-5bob'))