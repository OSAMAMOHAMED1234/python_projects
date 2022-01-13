def bubble_sort_for(array):
  tries = 0
  has_swapped = False
  for index in range(len(array)):
    for j in range(len(array) - index - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
        tries += 1
        has_swapped = True
    if has_swapped == False:
      break
  return array, tries
data = [10, 8, 2, 5, 6, 7, 4, 3, 1, 9]
print(bubble_sort_for(data))


def bubble_sort_while(array):
  is_swapped = True
  tries = 0
  total_iteration = 0 
  while is_swapped:
    is_swapped = False
    for i in range(len(array) - total_iteration - 1):
      if array[i] > array[i+1]:
        array[i], array[i + 1] = array[i + 1], array[i]
        tries += 1
        is_swapped = True
    total_iteration += 1
  return array, tries
data2 = [10, 8, 2, 5, 6, 7, 4, 3, 1, 9]
print(bubble_sort_while(data2))