import re 


for _ in range(int(input())):
  ccn = input()
  if re.search(r'^([4-6]{,1}[0-9]{1,3})(-*[0-9]{,4}){3}$', ccn) and len(ccn) >= 16 and len(ccn) <= 19:
    print('Invalid') if re.search(r'(\d)\1{3,}', ccn.replace('-','')) else print('Valid')
  else:
    print('Invalid')

# for _ in range(int(input())):
#   ccn = input()
#   if re.search(r'^([4-6]{,1}[0-9]{1,3})(-*[0-9]{,4}){3}$', ccn) and len(ccn) >= 16 and len(ccn) <= 19:
#     if re.search(r'(\d)\1{3,}', ccn.replace('-','')):
#       print('Invalid')
#     else:
#       print('Valid')
#   else:
#     print('Invalid')