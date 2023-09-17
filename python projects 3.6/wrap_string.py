import textwrap
def merge_the_tools(string, k):
  for i in textwrap.wrap(string, k):
    d = dict()
    # for c in i:
    #   if c not in d:
    #     d.setdefault(c, c) # d[c] = c
    # print('d=>', ''.join(d))
    print(''.join([ d.setdefault(c, c) for c in i if c not in d ]))  
merge_the_tools('AABCAAADA ', 3)
