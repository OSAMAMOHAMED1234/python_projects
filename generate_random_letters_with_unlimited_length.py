import random, string

def random_token(n):
  return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(n)])

print(random_token(250))