# capital(65, 91), small(97, 123), numbers(48, 58)
# alphabet = [chr(i) for i in range(48, 58)]
 

# for i in [chr(i) for i in range(65, 91)]:
#   print(f'{i} => {ord(i)}')


# ascii_lowercase, ascii_uppercase, digits
# import string
# alphabet = string.ascii_lowercase 


def rangoli(size):
  alphabet = [chr(char) for char in range(97, 123)]
  rangoli_list = []
  for letter in range(size):
    alpha_str = '-'.join(alphabet[letter:size])
    rangoli_list.append((alpha_str[::-1] + alpha_str[1:]).center(4 * size - 3, '-'))
  print('\n'.join(rangoli_list[:0:-1] + rangoli_list))

rangoli(6)