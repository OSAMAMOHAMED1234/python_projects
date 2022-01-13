def linear_search(array, target):
  tries = 0
  for index in range(len(array)):
    tries += 1
    if array[index] == target:
      return index, tries
  return None

print(linear_search([x for x in range(101)], 50))