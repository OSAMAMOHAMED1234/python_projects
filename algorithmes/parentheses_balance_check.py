def parentheses_balance_stack_check(expression):
  open_list, close_list, stack = ['[', '{', '('], [']', '}', ')'], []
  for i in expression:
    if i in open_list:
      stack.append(i)
    elif i in close_list:
      pos = close_list.index(i)
      if len(stack) > 0 and open_list[pos] == stack[len(stack) - 1]:
        stack.pop()
      else:
        return False
  return True if len(stack) == 0 else False
print(parentheses_balance_stack_check('((( [] [] )) () (()))'))
print(parentheses_balance_stack_check('((( [] [] )) () (())'))


def parentheses_balance_queue_check(expression): 
  open_tuple, close_tuple, queue = tuple('({['), tuple(')}]'), []
  map_dict = dict(zip(open_tuple, close_tuple))
  for i in expression:
    if i in open_tuple:
      queue.append(map_dict[i])
    elif i in close_tuple:
      if not queue or i != queue.pop():
        return False
  return True if not queue else False
print(parentheses_balance_queue_check('((( [] [] )) () (()))'))
print(parentheses_balance_queue_check('((( [] [] )) () (())'))