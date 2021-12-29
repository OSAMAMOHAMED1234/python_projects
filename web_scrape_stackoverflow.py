import requests
import time
import os
import pandas as pd
from requests_html import HTML


def clean_scraped_data(text, keyname=None):
  if keyname == 'votes':
    return text.replace('\nvotes', '')
  if keyname == 'answers':
    return text.replace('answers', '')
  if keyname == 'views':
    return text.replace(' views', '')
  if keyname == 'tags':
    return text.replace(' ', ', ')
  return text


def parse_tagged_page(html):
  question_summaries = html.find('.question-summary')
  key_names = ['question', 'votes', 'answers', 'views', 'short desription', 'tags', 'user details']
  classes_needed = ['.question-hyperlink', '.vote', '.status', '.views', '.excerpt', '.tags', '.user-details']
  datas = []
  for q_el in question_summaries:
    question_data = {}
    for i, _class in enumerate(classes_needed):
      sub_el = q_el.find(_class, first=True)
      keyname = key_names[i]
      question_data[keyname] = clean_scraped_data(sub_el.text, keyname=keyname)
    question_data['url'] = 'https://stackoverflow.com' + q_el.find('.question-hyperlink')[0].attrs['href']
    datas.append(question_data)
  return datas


def extract_data_from_url(url):
  r = requests.get(url)
  if r.status_code not in range(200, 299):
    return []
  html_str = r.text
  html = HTML(html=html_str)
  datas = parse_tagged_page(html)
  return datas


def scrape_tag(tag='python', query_filter='Votes', max_pages=50, pagesize=50):
  base_url = 'https://stackoverflow.com/questions/tagged/'
  datas = []
  for p in range(max_pages):
    page_num = p + 1
    url = f"{base_url}{tag}?tab={query_filter}&page={page_num}&pagesize={pagesize}"
    datas += extract_data_from_url(url)
    time.sleep(1.2)
  return datas
datas = scrape_tag(tag='python')

df = pd.DataFrame(datas)
df.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'python.csv'), index=False)



# columns = ['votes', 'num_answers', 'views', 'question', 'user']
# this_row = [1000, 500, 3000000, 'What does the "yield" keyword do?', 'OSAMA']
# row_data = dict(zip(columns, this_row))
# print(row_data)
# # for column, row_v in zip(columns, this_row):
# #   print(column, row_v)