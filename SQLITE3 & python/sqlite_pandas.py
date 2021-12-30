
import pickle
import pandas as pd

data = [{'name': 'OSAMA'}]
with open('users.pkl', 'wb') as f:
	pickle.dump(data, f)   

data_from_pkl = pickle.load(open('users.pkl', 'rb'))
print(data_from_pkl)
    
df = pd.DataFrame(data)
print(df.head())
df.to_pickle('df_pkl')
# df.to_csv('df_pkl')

df2 = pd.read_pickle('df_pkl')
print(df2.head())


class Movie:
	name = 'Unknown'
	genre = 'Action'
	def __init__(self, name='', genre='', *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.name = name
		self.genre = genre

from dataclasses import dataclass
@dataclass
class Movie:
	name:str = 'Unknown'
	genre:str = 'Action'
	year:int = 2010

movie_obj = Movie(name='moviename', genre='Sci-Fi')
print(movie_obj.name)
print(movie_obj.year)

print('==================================================')
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Movie(Base): # table scheme
	__tablename__ = 'movies' # table name
	id = Column(Integer, primary_key=True)
	name = Column(String)
	genre = Column(String)
	description = Column(String)
	year = Column(Integer, nullable=True)
	
	def __repr__(self):
		return f'<Movie name={self.name}>'

Base.metadata.create_all(engine) # create table


# # create
# movie_obj = Movie(name='Moviename', genre='Action')
# session.add(movie_obj) # pre save
# session.commit() # save
# print(movie_obj.id, movie_obj.name, movie_obj.genre, movie_obj.description)


# read
# read one
movie_obj = session.query(Movie).get(1) # id
print(movie_obj.id, movie_obj.name, movie_obj.genre, movie_obj.description)

# read all
qs = session.query(Movie).all()
print(qs)

# read all & filter by column value
qs = session.query(Movie).filter_by(name='Moviename').all()
print(qs)

# read all & filter by column value containing something
qs = session.query(Movie).filter(Movie.name.contains('name')).all()
print(qs)


# update
movie_obj = session.query(Movie).get(1)
movie_obj.description = 'movie description here'
session.commit()

qs = session.query(Movie).filter(Movie.name.contains('Moviename')).all()
for index, movie_obj in enumerate(qs):
	movie_obj.name = f'Movie-name {index + 1}'
session.commit()


# # delete
# movie_obj = session.query(Movie).get(2)
# session.delete(movie_obj)
# session.commit()

# session.flush()
print('==================================================')
import sqlacodegen
import pandas as pd
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app2.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
metadata = Base.metadata

class MovieApp2(Base):
	__tablename__ = 'movies'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	genre = Column(String)
	year = Column(Integer)
	def __repr__(self):
		return f'<Movie name={self.name}>'

qs = session.query(MovieApp2).all()
for old_obj in qs:
	movie_obj = Movie(name=old_obj.name, genre=old_obj.genre, year=old_obj.year)
	print(movie_obj.name)
	session.add(movie_obj)
session.commit()

old_engine = create_engine("sqlite:///app2.db")
old_df = pd.read_sql_table("movies", old_engine)
print(old_df.head())

current_engine = create_engine('sqlite:///app.db')
current_df = pd.read_sql_table('movies', current_engine)
print(current_df.head())


final_df = pd.concat([current_df, old_df])
print(final_df.head(n=20))

final_df = final_df[['name', 'genre', 'description', 'year']]
final_df.reset_index(inplace=True, drop=True)
print(final_df.head(n=20))

final_df.to_sql(
	'movies',
	current_engine,
	if_exists='replace', # fail, append
	dtype = {
		'name': String,
		'genre': String,
		'year': Integer,
		'description': String,
	}
)
# sqlacodegen sqlite:///app.db


print('==================================================')
import sqlite3
conx = sqlite3.connect('app.db')
conx2 = create_engine('sqlite:///app.db')
df = pd.read_sql_query('SELECT * FROM movies', conx2)
print(df.head())