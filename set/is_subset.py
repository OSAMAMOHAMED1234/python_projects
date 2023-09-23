n = int(input())
for _ in range(n):
  a = set(map(int, input().split()))
  b = set(map(int, input().split()))
  if a.issubset(b):
    print(True)
  else:
    print(False)