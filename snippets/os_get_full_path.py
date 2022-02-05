import os

# https://docs.python.org/3.9/library/os.path.html


# list of dirs, files
print(os.listdir())


# file size
print(os.path.getsize(os.path.abspath(__file__)))


# user dir
print(os.path.expanduser('~')) # user dir


# username
print(os.path.expandvars('%userprofile%'))
print(os.path.expanduser('~').split('\\')[-1])
print(os.path.split(os.path.expanduser('~'))[-1])
print(os.getlogin())
print(os.environ.get('USERNAME')) # os.environ.get('USER')
print(os.getenv('SUDO_USER', os.getenv('USERNAME')))


# current working dir
print(os.getcwd())


# dir
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.realpath(__file__)))


# full path
print(os.path.abspath(__file__))
print(os.path.realpath(__file__))


# filename.ext
fname1 = os.path.basename('url/filename.ext') # filename.ext => download url itself
fname2 = os.path.basename(__file__) # filename.ext
fname3 = 'url/filename.ext'.split('/')[-1]
print(fname1)
print(fname2)
print(fname3)


# .ext
extension = os.path.splitext('filename.ext')[1] # .ext => filename
print(extension)


# THIS_FILE_PATH = os.path.abspath(__file__)
# BASE_DIR = os.path.dirname(THIS_FILE_PATH)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(os.path.join(BASE_DIR, 'folder name', 'another folder name'))


os.makedirs(os.path.join(BASE_DIR, 'folder name'), exist_ok=True) # create if not exists, no errors if exists, False = error if exists #=> os.path.exists()

# os.mkdir(os.path.join(BASE_DIR, 'folder name')) # create if not exists, error if exists => FileExistsError


# rename dir, file
os.rename(os.path.join(BASE_DIR, 'folder name'), os.path.join(BASE_DIR, 'new folder name')) # error if exists => FileExistsError
os.rename(os.path.join(BASE_DIR, 'test.txt'), os.path.join(BASE_DIR, 'new.txt')) # error if not found => FileNotFoundError


# check if dir, file is exists => True, False
print(os.path.isdir(os.path.abspath(__file__)))
print(os.path.isfile(os.path.abspath(__file__)))


# remove dir, file
# os.remove(os.path.join(BASE_DIR, 'folder name'))
# os.rmdir(os.path.join(BASE_DIR, 'folder name'))
# os.remove(os.path.join(BASE_DIR, 'new.txt'))

# os.removedirs(os.path.abspath(__file__))


for i in range(1, 6):
  fname = f'{i}.txt'
  full_path = os.path.join(BASE_DIR, 'test', fname)
  if os.path.exists(full_path):
    print(f'skipped {fname}')
    continue
  with open(full_path, 'w') as f:
    print(f'created {fname}')
    f.write('Hello OSAMA!')
    f.close()