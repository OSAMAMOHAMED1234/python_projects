import requests
from time import sleep

api_key = '' # https://pro.coinmarketcap.com/account
bot_key = '' # botFather HTTP API:
price_limit = 70000
time_interval = 60
telegram_chat_ids = ['', '', ] # IDBot


def get_price():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'1',
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
  }
  response = requests.get(url, headers=headers, params=parameters).json()
  btc_price = response.get('data')[0].get('quote').get('USD').get('price')
  btc_time = response.get('data')[0].get('quote').get('USD').get('last_updated')
  return btc_price, btc_time[:10], btc_time[11:19]


def send_price(chat_id, msg):
  url = f'https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}'
  return requests.get(url).status_code


while True:
  price = get_price()
  if int(price[0]) < price_limit:
    for te_id in telegram_chat_ids:
      send_price(te_id, f'Bitcoin Price is: {price[0]:.2f}$ \nat: {price[1]} {price[2]}')
  sleep(time_interval)