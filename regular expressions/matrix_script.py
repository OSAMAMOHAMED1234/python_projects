import re


first_multiple_input = input().rstrip().split()
row, col, matrix = int(first_multiple_input[0]), int(first_multiple_input[1]), []

for _ in range(row):
  matrix_item = input()
  matrix.append(matrix_item)

encoded_string = ''.join([matrix[r][c] for c in range(col) for r in range(row)])
# encoded_string = ''
# for c in range(col):
#   for r in range(row):
#     print(matrix[r][c])
#     encoded_string += ''.join(matrix[r][c])
pattren = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
print(re.sub(pattren, ' ', encoded_string))