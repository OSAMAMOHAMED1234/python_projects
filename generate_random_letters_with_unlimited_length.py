import random, string

def random_token(n):
  # limited_punctuation = random.sample(string.punctuation, 3)  # Gets 3 random punctuation marks
  limited_punctuation = '!@#$%^&*'
  choices = string.ascii_letters + string.digits + ''.join(limited_punctuation)
  return ''.join([random.choice(choices) for _ in range(n)])
print(random_token(int(50)))

def random_token(n):
  return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(n)])
print(random_token(250))


def random_token(n):
  max_num_of_punc = 3
  limited_punctuation = '!@#$%^&*'
  token_part1 = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(n - max_num_of_punc)])
  token_part2 = ''.join([random.choice(limited_punctuation) for _ in range(max_num_of_punc)])
  choices = token_part1 + token_part2
  return ''.join(random.sample(choices, len(choices)))
print(random_token(50))


class RandomSerialGenerator:
  def __init__(self, length=10, characters=string.ascii_letters + string.digits + string.punctuation):
    self.length = length
    self.characters = characters

  def generate(self):
    return ''.join([random.choice(self.characters) for _ in range(self.length)])  
serial_generator = RandomSerialGenerator(length=50)
serial = serial_generator.generate()
print(serial)
