import re, email.utils


n = int(input())
for _ in range(n):
  s = input()
  parsed_address = email.utils.parseaddr(s)
  res = re.match(r'^[a-z][A-z0-9\.-]+@[a-z]+\.[a-z]{,3}$', parsed_address[1].strip())
  if res != None:
    print(email.utils.formataddr(parsed_address))