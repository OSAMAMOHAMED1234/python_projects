# x, y, z, n = (int(input()) for _ in range(4))
def list_comprehensions(x, y, z, n):
  # res = []
  # for a in range(x + 1):
  #   for b in range(y + 1):
  #     for c in range(z + 1):
  #       if a + b + c != n:
  #         res.append([a, b, c])
  # print(res)
  print([ [a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n ])
list_comprehensions(2, 2, 2, 2)