from requests.api import options
from requests_html import HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url = 'https://www.amazon.com/Seagate-Portable-External-Hard-Drive/dp/B07CRG94G3/'
title_lookup = '#productTitle'
price_lookup = '#price_inside_buybox'

driver.get(url)
body_el = driver.find_element_by_css_selector('body')
html_str = body_el.get_attribute('innerHTML')
html_obj = HTML(html=html_str)
product_title = html_obj.find(title_lookup, first=True).text
product_price = html_obj.find(price_lookup, first=True).text