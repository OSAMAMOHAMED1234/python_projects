def runner_up(n, lis):
  scores = list(lis)
  scores.sort()
  for _ in range(n):
    if scores[-1] == scores[-2]:
      scores.pop(-1)
  print(scores[-2])
 

n = int(input())
arr = map(int, input().split())
runner_up(n, arr)