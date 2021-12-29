from getpass import getpass
name = input("What's your name?\n")
password = getpass("What's your password?\n")
print(name, password)

# ==================================================

import sys
if __name__== '__main__':
  try:
    name = sys.argv[1] # positional args
  except:
    name = input("What's your name?\n")
  from getpass import getpass
  password = getpass("What's your password?\n")
  print(name, password)

# ==================================================

import argparse
def my_const_fun(*args, **kwargs):
  print('const', args, kwargs)
def my_default_fun(*args, **kwargs):
  print('default', args, kwargs)
if __name__== '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('integers', type=int, nargs='+') # named args, nargs + => more than one args
  parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max) # get max, otherwise sum if --sum
  parser.add_argument('--math', dest='math_is_fun', action='store_const', const=my_const_fun, default=my_default_fun) # get my_default_fun, otherwise my_const_fun if --math
  args = parser.parse_args()
  print(args.integers)
  print(args.accumulate(args.integers))
  print(args.math_is_fun(args.integers))

# ==================================================

import fire
def hello(name='OSAMA'): # --name
  return f'Hello {name}'
if __name__ == '__main__':
  fire.Fire(hello)

# ==================================================

from getpass import getpass
import fire
def login(name=None):
  if name == None:
    name = input("What's your name?\n")
  password = getpass("What's your password?\n")
  return name, password
if __name__ == '__main__':
  fire.Fire(login)

# ==================================================

import fire
def scrape_tag(tag='python', query_filter='Votes', max_pages=5, pagesize=25): #  --max_pages 10 --tag "js"
  base_url = 'https://stackoverflow.com/questions/tagged/'
  datas = []
  for p in range(max_pages):
    page_num = p + 1
    url = f'{base_url}{tag}?tab={query_filter}&page={page_num}&pagesize={pagesize}'
    datas.append(url)
  return datas
if __name__ == '__main__':
  fire.Fire(scrape_tag)

# ==================================================

import fire
from getpass import getpass
class Auth(object):
  def login(self, username=None): # auth login --username "OSAMA"
    if username == None:
      username = input('Username: ')
    if username == None:
      print('A username is required')
      return
    password = getpass('Password: ')
    return username, password

def login(username=None): # login --username "OSAMA"
  if username == None:
    username = input('Username: ')
  if username == None:
    print('A username is required')
    return
  password = getpass('Password: ')
  return username, password
    
def scrape_tag(tag='python', query_filter='Votes', max_pages=50, pagesize=25): # scrape --tag "js" --max_pages "5"
  base_url = 'https://stackoverflow.com/questions/tagged/'
  datas = []
  for p in range(max_pages):
    page_num = p + 1
    url = f'{base_url}{tag}?tab={query_filter}&page={page_num}&pagesize={pagesize}'
    datas.append(url)
  return datas

class Pipeline(object):
  def __init__(self):
    self.login = login # login --username "OSAMA"
    self.scrape = scrape_tag # scrape --tag "js" --max_pages "5"
    self.auth = Auth() # auth login --username "OSAMA"

if __name__ == '__main__':
  fire.Fire(Pipeline)

# ==================================================

import inspect
from collections import OrderedDict
def rando_fn(abc, df=123):
  print(abc, df)
sig = inspect.signature(rando_fn)
# print(sig.parameters.items())
# print(sig.parameters.keys())
# print(sig.parameters.values())


def get_signature(fn):
  params = inspect.signature(fn).parameters
  args = []
  kwargs = OrderedDict()
  for p in params.values():
    if p.default is p.empty:
      args.append(p.name)
    else:
      kwargs[p.name] = p.default
  return {'args': args, 'kwargs': kwargs}
print(get_signature(rando_fn))