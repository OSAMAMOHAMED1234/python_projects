import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CACHE_DIR = os.path.join(BASE_DIR, 'cache')
os.makedirs(CACHE_DIR, exist_ok=True)


new_dataframes = []
csv_files = [x for x in sorted(os.listdir(DATA_DIR), reverse=True) if x.endswith(".csv")]
for filename in csv_files:
  year = filename.replace(".csv", "")
  csv_path = os.path.join(DATA_DIR, filename)
  this_df = pd.read_csv(csv_path)
  this_df['filename'] = filename
  this_df['year'] = year
  new_dataframes.append(this_df)


all_dataframes = pd.concat(new_dataframes)
dataset = os.path.join(CACHE_DIR, 'movies-box-office-dataset.csv')
all_dataframes.to_csv(dataset, index=False)