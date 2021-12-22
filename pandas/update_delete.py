import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(BASE_DIR, 'cache')
working_file = os.path.join(CACHE_DIR, 'movies-box-office-dataset.csv')
output_file = os.path.join(CACHE_DIR, 'movies-box-office-dataset-cleaned.csv')

df = pd.read_csv(working_file)
df.drop(['%', '%.1'], axis=1, inplace=True)
# df.drop(columns=['%', '%.1']) # not work
# df['Worldwide'] = df['Worldwide'].replace("$", "").replace(",", "") # not work

def currency_str_to_int(current_val):
  currency_val = current_val.replace("$", "").replace(",", "")
  try:
    currency_val = int(currency_val)
  except:
    currency_val = 0
  return currency_val 


def clean_col(row):
  for col in ['Worldwide', 'Domestic', 'Foreign']:
    current_val = row[col]
    row[col] = currency_str_to_int(current_val)
  return row


df_cleaned = df.apply(clean_col, axis=1) # update
df_cleaned.sort_values(by=['Worldwide'], inplace=True, ascending=False) # sort
df_cleaned.reset_index(inplace=True, drop=True) # reset index based on a new sort
df_cleaned['Rank'] = df_cleaned.index + 1 # set rank after a new sort
df_cleaned['Domestic %'] = df_cleaned['Domestic'] / df_cleaned['Worldwide'] # update column
df_cleaned['Foreign %'] = df_cleaned['Foreign'] / df_cleaned['Worldwide']
df_cleaned.to_csv(output_file, index=False) # create a csv file