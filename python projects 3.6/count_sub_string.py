def count_substring(string, sub_string):
  count = 0
  for i in range(len(string) - len(sub_string) + 1):
    if string[i: i + len(sub_string)] == sub_string:
      count += 1
  return count


# def count_substring(string, sub_string):
#   count = 0
#   for i in range(len(string)-(len(sub_string)-1)):
#     if sub_string == string[i:len(sub_string)+i]:
#       count += 1
#   return count


# def count_substring(string, sub_string):
#   res = sum(1 for i in range(len(string)) if string.startswith(sub_string, i))
#   return res


# def count_substring(string, sub_string):
#   count, start = 0, 0
#   while start < len(string):
#     pos = string.find(sub_string, start)
#     if pos != -1:
#       start = pos + 1
#       count += 1
#     else: 
#       break
#   return count


string = 'ABCDCDC'
print('Number of substrings', count_substring(string, 'CDC'))