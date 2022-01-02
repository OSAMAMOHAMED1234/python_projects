import os
from flask import Flask
from .resources import get_resource_path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = get_resource_path('data')
IMG_PATH = os.path.join(DATA_DIR, '1.jpg')
web_app = Flask(__name__)

@web_app.route('/', methods=['GET'])
def index():
  return {
  'dir': str(BASE_DIR), 
  'data_dir': str(DATA_DIR),
  'img_path': os.path.isfile(IMG_PATH),
  }, 200