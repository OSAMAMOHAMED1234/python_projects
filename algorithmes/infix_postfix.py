def infix_to_postfix(expression):
  operators = set(['+', '-', '*', '/', '(', ')', '^'])
  priority = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}
  stack, output = [], ''
  for i in expression:
    if i not in operators:
      output += i
    elif i == '(':
      stack.append('(')
    elif i == ')':
      while stack and stack[-1] != '(':
        output += stack.pop()
      stack.pop()
    else:
      while stack and stack[-1] != '(' and priority[i] <= priority[stack[-1]]:
        output += stack.pop()
      stack.append(i)
  while stack:
    output += stack.pop()
  return output
print(infix_to_postfix('A+B*(C^D-E)^(F+G*H)-I'))


def evaluate_postfix(expression):
  stack = []
  for i in expression: 
    if i.isdigit():
      stack.append(i)
    else:
      val1 = stack.pop()
      val2 = stack.pop()
      stack.append(str(eval(val2 + i + val1)))
  return stack.pop()
print(evaluate_postfix('6 3 4 * + 2 -'.split(' ')))


def postfix_to_infix(expression) :
  stack = []
  for i in expression:    
    if i.isalpha():
      stack.append(i)
    else:
      op1 = stack.pop()
      op2 = stack.pop()
      stack.append('(' + op2 + i + op1 + ')')
  return stack[0]
print(postfix_to_infix('ABCD^E-FGH*+^*+I-'))