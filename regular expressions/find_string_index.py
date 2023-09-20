import re


string, sub_string = input(), input()
matches = list(re.finditer(r'(?={})'.format(sub_string), string))
if matches:
  print('\n'.join(str((match.start(), match.start() + len(sub_string) - 1)) for match in matches))
else:
  print('(-1, -1)')