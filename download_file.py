import os
import requests
import shutil


url = ''


def download_file_basic(url):
  fname = os.path.basename(url)
  dr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
  r = requests.get(url, stream=True)
  r.raise_for_status()
  with open(dr_path, 'wb') as f:
    f.write(r.content)
    f.close()
  return dr_path
download_file_basic(url)


def download_file_faster(url, directory=None, fname=None):
  if fname == None:
    fname = os.path.basename(url)
  else:
    extension = os.path.splitext(os.path.basename(url))[1]
    fname += extension
  if directory == None:
    dr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
  else:
    dr_path = os.path.join(directory, fname)
  with requests.get(url, stream=True) as r: # True = keep open until done
    try:
      r.raise_for_status() # give error if status_code != 200
    except requests.exceptions.RequestException as e: # handle all types of errors
      print('error', e)
    with open(dr_path, 'wb') as file_obj:
      shutil.copyfileobj(r.raw, file_obj)
  return dr_path
download_file_faster(url)


def download_file_slower(url):
  fname = url.split('/')[-1]
  dr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
  with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(dr_path, 'wb') as f:
      for chunk in r.iter_content(chunk_size=8192):
        if chunk:
          f.write(chunk)
  return dr_path
download_file_slower(url)