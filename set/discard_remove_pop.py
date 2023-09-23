n = int(input())
set_nums = set(map(int, input().split()))
for _ in range(int(input())):
  command = input().split()
  if command[0] == 'pop':
    set_nums.pop()
  elif command[0] == 'remove':
    set_nums.remove(int(command[1]))
  elif command[0] == 'discard':
    set_nums.discard(int(command[1]))
  
print(sum(set_nums))