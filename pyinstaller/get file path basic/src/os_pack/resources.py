import sys
import os

def get_resource_path(relative_path):
  dev_base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  base_path = getattr(sys, '_MEIPASS', dev_base_path)
  return os.path.join(base_path, relative_path)