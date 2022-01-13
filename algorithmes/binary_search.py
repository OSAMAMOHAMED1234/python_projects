def binary_search(array, target):
  start = 0
  middle = 0
  end = len(array) - 1
  tries = 0
  while start <= end:
    middle = (start + end) // 2
    tries += 1
    if array[middle] < target:
      start = middle + 1
    elif array[middle] > target:
      end = middle - 1
    else:
      return middle, tries
  return None
print(binary_search([x for x in range(101)], 50))