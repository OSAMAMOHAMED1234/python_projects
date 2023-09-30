import random, string

def random_token(n):
  return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(n)])
print(random_token(250))


class RandomSerialGenerator:
  def __init__(self, length=10, characters=string.ascii_letters + string.digits + string.punctuation):
    self.length = length
    self.characters = characters

  def generate(self):
    return ''.join([random.choice(self.characters) for _ in range(self.length)])  
serial_generator = RandomSerialGenerator(length=50)
serial = serial_generator.generate()
print(serial)
