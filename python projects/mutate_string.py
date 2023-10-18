def mutate_string(string, position, character):
  string = string[:position] + character + string[position+1:]
  return string
print(mutate_string('abracadabra', 5, 'k'))


def mutate_string(string, position, character):
  string = list(string)
  string[position] = character
  string = ''.join(string)
  return string
print(mutate_string('abracadabra', 5, 'k'))