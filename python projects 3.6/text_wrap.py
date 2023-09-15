# from textwrap import fill
# def wrap(string, max_width):
#   return fill(string, max_width)


def wrap(string, max_width):
  res = []
  for i in range(0, len(string), max_width):
    res.append(string[i:i + max_width])
  return '\n'.join(res)

print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))