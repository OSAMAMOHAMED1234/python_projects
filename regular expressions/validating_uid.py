import re 


for _ in range(int(input())):
  uid = input()
  c1 = len(re.findall(r'[A-Z]', uid)) >= 2
  c2 = len(re.findall(r'(?=[0-9]){3,}', uid)) >= 3
  c3 = len(re.findall(r'[a-zA-Z0-9]', uid)) == len(uid)
  c4 = len(set(uid)) == len(uid)
  c5 = len(uid) == 10
  print('Valid' if all([c1, c2, c3, c4, c5]) else 'Invalid')


regex = r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[\w]{10}$'
for i in range(int(input())):
  uid = input()
  print('Valid') if re.match(regex, uid) else print('Invalid') 