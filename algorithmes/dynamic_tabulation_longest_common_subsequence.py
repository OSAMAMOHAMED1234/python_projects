def longest_common_subsequence_dynamic_tabulation(s1, s2):
  m, n = len(s1), len(s2)
  table = [['' for x in range(n)] for x in range(m)]
  for i in range(m):
    for j in range(n):
      if s1[i] == s2[j]:
        if i == 0 or j == 0:
          table[i][j] = s1[i]
        else:
          table[i][j] = table[i - 1][j - 1] + s1[i]
      else:
        table[i][j] = max(table[i - 1][j], table[i][j - 1], key=len)
  cs = table[-1][-1]
  return len(cs), [*cs]
print(longest_common_subsequence_dynamic_tabulation(['A', 'B', 'C', 'B', 'D', 'A', 'B'], ['B', 'D', 'C', 'A', 'B', 'A']))


def lcs(s1, s2):
  m, n = len(s1), len(s2)
  table = [[0 for i in range(n + 1)] for i in range(m + 1)]
  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0 or j == 0 :
        table[i][j] = 0
      elif s1[i - 1] == s2[j - 1]:
        table[i][j] = table[i - 1][j - 1] + 1
      else:
        table[i][j] = max(table[i - 1][j], table[i][j - 1])
  return table[m][n]
print(lcs(['A', 'B', 'C', 'B', 'D', 'A', 'B'], ['B', 'D', 'C', 'A', 'B', 'A']))