def minimum_number_of_coins(value, coins=[1, 5, 10, 20, 50, 100, 200]):
  money_list = []
  for coin in sorted(coins, reverse=True):
    while value >= coin:
      value = value - coin
      money_list.append(coin)
      money_dict = {f'{i} LE' : money_list.count(i) for i in money_list}
  return money_dict, money_list, len(money_list)
print(minimum_number_of_coins(788))


def min_coin(value, coins=[1, 5, 10, 20, 50, 100, 200], cache={}):
  coins = sorted(coins, reverse=True)
  if value in cache:
    return cache[value]
  elif value in coins:
    cache[value] = [value]
    return [value]
  elif min(coins) > value:
    cache[value] = []
    return []
  else:
    min_configuration = []
    for coin in coins:
      results = min_coin(value - coin, coins, cache=cache)
      if results and (not min_configuration or (1 + len(results)) < len(min_configuration)):
        min_configuration = [coin] + results
    cache[value] = min_configuration
  return cache[value]
print(min_coin(788))

def df(value):
  money_list = min_coin(value)
  money_dict = {f'{i} LE' : money_list.count(i) for i in money_list}
  return money_dict, money_list, len(money_list)
print(df(788))