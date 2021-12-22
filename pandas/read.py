import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.listdir(DATA_DIR)


my_data = os.path.join(DATA_DIR, '2019.csv')
df = pd.read_csv(my_data)
print(df.head(n=10)) # read first 10 rows
print(df.tail(n=10)) # read lst 10 rows
print(df.head())
print(df['Release Group']) # read column
print(df['Worldwide']) # read column

# print(df[0]) # error
print(df.iloc[0]) # read fisrt row
print(df.dtypes) # get type
print(df.to_dict("Rank")) # order by rank column to use in rest api



# # basic example
# my_items = [{"category": "Action", "title": "My awesome movie"}, {"category": "Comedy", "title": "Data Jokes are Us"}]
# df = pd.DataFrame(my_items)
# print(df.head())
# print(df['category'])
# print(df['title'])
# print(df[0]) # error
# print(df.iloc[0])