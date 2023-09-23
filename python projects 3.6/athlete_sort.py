n, m = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
k = int(input())
for i in sorted(arr, key=lambda x: x[k]):
  print(*i)