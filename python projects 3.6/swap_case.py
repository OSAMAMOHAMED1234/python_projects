string = 'HackerRank.com presents "Pythonist 2".'
print(string.swapcase())

def swap_case(s):
  string = []
  for l in s:
    string.append(l.upper()) if l.islower() else string.append(l.lower())
    # if l.islower():
    #   string.append(l.upper())
    # else:
    #   string.append(l.lower())
  return ''.join(string)
print(swap_case('HackerRank.com presents "Pythonist 2".'))

def swap_case(s):
  string = ''
  for l in s:
    if l.islower():
      string += l.upper()
    else:
      string += l.lower()
  return string
print(swap_case('HackerRank.com presents "Pythonist 2".'))