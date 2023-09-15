# capital(65, 91), small(97, 123), numbers(48, 58)
# alphabet = [chr(i) for i in range(48, 58)]
 

# for i in [chr(i) for i in range(65, 91)]:
#   print(f'{i} => {ord(i)}')


# ascii_lowercase, ascii_uppercase, digits
# import string
# alphabet = string.ascii_lowercase 


def print_rangoli(size):
  alphabet = [chr(i) for i in range(97, 123)]
  rangoli_list = []
  for i in range(size):
    s = '-'.join(alphabet[i:size])
    rangoli_list.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))
  print('\n'.join(rangoli_list[:0:-1] + rangoli_list))

print_rangoli(5)