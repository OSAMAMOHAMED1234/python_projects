import re 


s = input()

vowels = 'AEIOUaeiou'
consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
reg = re.compile(f'(?<=[{consonants}])([{vowels}]'+ '{2,}' + f')(?=[{consonants}])')
res = re.findall(reg, s)
# res = reg.findall(s)
print('\n'.join(res)) if len(res) >= 1 else print(-1)
