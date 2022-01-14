def insertion_sort(array):
  tries = 0
  for index in range(1, len(array)):
    key = array[index]
    j = index - 1
    while j >= 0 and key < array[j]:
      array[j + 1] = array[j]
      j -= 1
      tries += 1
    array[j + 1] = key
  return array, tries

data = [10, 8, 2, 5, 6, 7, 4, 3, 1, 9]
print(insertion_sort(data))