def doormat(height, width):
  result_list = []
  for i in range(height // 2):
    result_list.append(('.|.' * (2 * i + 1)).center(width, '-'))
  return print('\n'.join(result_list + ['WELCOME'.center(width, '-')] + result_list[::-1]))

doormat(7, 21)
# num1, num2 = map(int,input().split())
# print_door_mat(num1, num2)