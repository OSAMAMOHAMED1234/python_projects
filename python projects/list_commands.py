n = int(input())
res = []
while n > 0:
  q = list(map(str, input().split()))
  if q[0] == 'print':
    print(res)
  elif q[0] == 'insert':
    res.insert(int(q[1]), int(q[2]))
  elif q[0] == 'remove':
    res.remove(int(q[1]))
  elif q[0] == 'append':
    res.append(int(q[1]))
  elif q[0] == 'sort':
    res.sort()
  elif q[0] == 'pop':
    res.pop()
  elif q[0] == 'reverse':
    res.reverse()
  n -= 1