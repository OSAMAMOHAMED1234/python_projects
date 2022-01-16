def matrix_chain_multiplication_dynamic_tabulation(p):
  n = len(p)
  table = [[0 for x in range(n)] for x in range(n)]
  for i in range(1, n):
    table[i][i] = 0
  for L in range(2, n):
    for i in range(1, n - L + 1):
      j = i + L - 1
      table[i][j] = 10 ** 10
      for k in range(i, j):
        q = table[i][k] + table[k + 1][j] + p[i - 1] * p[k] * p[j]
        if q < table[i][j]:
          table[i][j] = q
  return table[1][n - 1]
print(matrix_chain_multiplication_dynamic_tabulation([4, 10, 3, 12, 20, 7]))