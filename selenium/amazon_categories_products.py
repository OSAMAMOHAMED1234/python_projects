import re
import time
import datetime
import pandas as pd

from pathlib import Path
from requests_html import HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_DIR = Path.cwd()
DATA_DIR = BASE_DIR / "data" # os.path.join(BASE_DIR, 'data')
if not DATA_DIR.exists(): # os.path.exists(DATA_DIR)
  DATA_DIR.mkdir(exist_ok=True) # os.makedirs(DATA_DIR, exist_ok=True)
    
product_category_links_output = DATA_DIR / "category-products.csv"
product_output = DATA_DIR / "products.csv"
options = Options()
options.add_argument("--headless")
options.add_argument('--log-level=1')

driver = webdriver.Chrome(options=options)

categories = [
  {
    "name": "toys-and-games", 
    "url": "https://www.amazon.com/Best-Sellers-Toys-Games/zgbs/toys-and-games/"
  },
  {
    "name": "electronics", 
    "url": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/"
  },
  {
    "name": "fashion", 
    "url": "https://www.amazon.com/Best-Sellers/zgbs/fashion/"
  }
]

regex_options = [
  r"https://www.amazon.com/gp/product/(?P<product_id>[\w-]+)/",
  r"https://www.amazon.com/dp/(?P<product_id>[\w-]+)/",
  r"https://www.amazon.com/(?P<slug>[\w-]+)/dp/(?P<product_id>[\w-]+)/",
]

def extract_product_id_from_url(url):
  product_id = None
  for regex_str in regex_options:
    regex = re.compile(regex_str)
    match = regex.match(url)
    if match != None:
      try:
        product_id = match['product_id']
      except:
        pass
  return product_id

def clean_page_links(page_links=[], category=None):
  final_page_links = []
  for url in page_links:
    product_id = extract_product_id_from_url(url)
    if product_id != None:
      final_page_links.append({"url": url, "product_id": product_id, "category": category})
  return final_page_links

def scrace_category_product_links(categories=[]):
  all_product_links = []
  for category in categories:
    time.sleep(1.5)
    url = category.get("url")
    driver.get(url)
    body_el = driver.find_element_by_css_selector("body")
    html_str = body_el.get_attribute("innerHTML")
    html_obj = HTML(html=html_str)
    page_links = [f"https://www.amazon.com{x}" for x in html_obj.links if x.startswith("/")]
    cleaned_links = clean_page_links(page_links=page_links, category=category)
    all_product_links += cleaned_links
  return all_product_links

def extract_categories_and_save(categories=[]):
  all_product_links = scrace_category_product_links(categories)
  category_df = pd.DataFrame(all_product_links)
  category_df.to_csv(product_category_links_output, index=False)

extract_categories_and_save(categories=categories)


def scrape_product_page(url, title_lookup="#productTitle", price_lookup="#price_inside_buybox"):
  driver.get(url)
  time.sleep(1.5)
  body_el = driver.find_element_by_css_selector("body")
  html_str = body_el.get_attribute("innerHTML")
  html_obj = HTML(html=html_str)
  product_title = html_obj.find(title_lookup, first=True).text
  product_price = html_obj.find(price_lookup, first=True).text
  print('product_price', product_price)
  return product_title, product_price

def row_scrape_event(row, *args, **kwargs):
  link = row['url']
  scraped = 0
  try:
    scraped = row['scraped']
  except:
    pass
  if scraped == 1 or scraped == "1":
    print("skipped")
    return row
  product_id = row['product_id']
  title, price = (None, None)
  try:
    title, price = scrape_product_page(link)
  except:
    pass
  row['title'] = title
  row['price'] = price
  row['scraped'] = 1
  row['timestamp'] = datetime.datetime.now().timestamp()
  return row

df = pd.read_csv(product_category_links_output)
# print(df.shape)

df_sub = df.copy() # df.head(n=10)
df_sub = df_sub.apply(row_scrape_event, axis=1)
df.to_csv(product_output, index=False)

products_df = pd.read_csv(product_output)
final_df = pd.concat([products_df, df_sub])
final_df.to_csv(product_output, index=False)