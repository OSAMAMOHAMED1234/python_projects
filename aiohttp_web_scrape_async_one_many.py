import asyncio
from aiohttp import ClientSession
import os

async def main():
	url = 'https://www.boxofficemojo.com/year/2020/'
	html_body = ''
	async with ClientSession() as session:
		async with session.get(url) as response:
			html_body = await response.read()
			return html_body

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
html_data = asyncio.run(main())
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'movies')
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, '2020.html')
with open(output_file, 'wb') as f:
	f.write(html_data)

print("==================================================")
import asyncio
from aiohttp import ClientSession
import os

async def fetch(url, session, year):
	async with session.get(url) as response:
		html_body = await response.read()
		return {'body': html_body, 'year': year}


async def main(start_year=2020, years_ago=5):
	tasks = []
	async with ClientSession() as session:
		for i in range(0, years_ago):
			year = start_year - i
			url = f'https://www.boxofficemojo.com/year/{year}/'
			tasks.append(
				asyncio.create_task(
					fetch(url, session, year)
				)
			)
		pages_content = await asyncio.gather(*tasks)
		return pages_content

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
results = asyncio.run(main())
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'movies', 'multi')
os.makedirs(output_dir, exist_ok=True)

for result in results:
	year = result.get('year')
	html_data = result.get('body')
	output_file = os.path.join(output_dir, f'{year}.html')
	with open(output_file, 'wb') as f:
		f.write(html_data)

print("==================================================")
# mulit with semaphore
import asyncio
from aiohttp import ClientSession
import os

async def fetch(url, session, year=None):
	async with session.get(url) as response:
		html_body = await response.read()
		return {'body': html_body, 'year': year}


async def fetch_with_sem(sem, session, url, year=None):
	async with sem:
		return await fetch(url, session, year)


async def main(start_year=2020, years_ago=20):
	tasks = []
	sem = asyncio.Semaphore(10)
	async with ClientSession() as session:
		for i in range(0, years_ago):
			year = start_year - i
			url = f'https://www.boxofficemojo.com/year/{year}/'
			print('year', year, url)
			tasks.append(
				asyncio.create_task(
					fetch_with_sem(sem, session, url, year=year)
				)
			)
		pages_content = await asyncio.gather(*tasks)
		return pages_content

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
results = asyncio.run(main())
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'movies', 'multi', 'semaphore')
os.makedirs(output_dir, exist_ok=True)

for result in results:
	year = result.get('year')
	html_data = result.get('body')
	output_file = os.path.join(output_dir, f'{year}.html')
	with open(output_file, 'wb') as f:
		f.write(html_data)