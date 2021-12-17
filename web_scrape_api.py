import requests
import pandas as pd
import pprint
import os

api_key = '' # https://www.themoviedb.org/settings/api
search_query = 'the matrix'
endpoint = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={search_query}'
r = requests.get(endpoint)
# pprint.pprint(r.json()) # pretty print json
if r.status_code in range(200, 299):
  data = r.json()
  results = data['results']
  if len(results) > 0:
    movie_ids = set()
    for result in results:
      _id = result['id']
      movie_ids.add(_id)
    movie_data = []
    for movie_id in movie_ids:
      endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
      r = requests.get(endpoint)
      if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)
    df = pd.DataFrame(movie_data)
    path = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, 'movies.csv')
    df.to_csv(filepath, index=False)