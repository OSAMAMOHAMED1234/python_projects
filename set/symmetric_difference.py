a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(a.symmetric_difference(b))) # ^



# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# set_a_diff = a.difference(b)
# set_b_diff = b.difference(a)
# new_set = sorted(set_a_diff.union(set_b_diff))
# for i in new_set:
#   print(i)