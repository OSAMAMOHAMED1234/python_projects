def fractional_knapsack(weights, values, capacity):
  res, weight_sum = 0, sum(weights)
  print(f'Over capacity: {capacity}, maximum: {weight_sum}') if capacity > weight_sum else ''
  for pair in sorted(zip(weights, values), key=lambda x: - x[1]/x[0]):
    if not bool(capacity):
      break
    if pair[0] > capacity:
      res += int(pair[1] / (pair[0] / capacity))
      capacity = 0
    elif pair[0] <= capacity:
      res += pair[1]
      capacity -= pair[0]
  return int(res)
print(fractional_knapsack([10, 20, 30], [60, 100, 120], 50))


def fractional_knapsack2(weights, values, capacity):
  res = 0
  for i in sorted(zip(weights, values)):
    if capacity - i[0] >= 0:
      capacity -= i[0]
      res += i[1]
    else:
      fraction = capacity / i[0]
      res += i[1] * fraction
      capacity = int(capacity - (i[0] * fraction))
      break
  return int(res)
print(fractional_knapsack2([10, 20, 30], [60, 100, 120], 50))