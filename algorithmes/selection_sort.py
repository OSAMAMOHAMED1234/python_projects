def selection_sort_for(array):
  tries = 0
  is_swapped = False
  for index in range(len(array)):
    min_index = index
    for i in range(index + 1, len(array)):
      if array[i] < array[min_index]:
        min_index = i
        tries += 1
        is_swapped = True
    array[index], array[min_index] = array[min_index], array[index]
    if is_swapped == False:
      break
  return array, tries

data = [10, 8, 2, 5, 6, 7, 4, 3, 1, 9]
print(selection_sort_for(data))


def selection_sort_while(array):
  tries = 0
  start = 0
  is_swapped = True
  while is_swapped:
    is_swapped = False
    for index in range(start + 1 , len(array)):
      if array[start] > array[index]:
        array[index], array[start] = array[start], array[index]
        tries += 1
        is_swapped = True
    start += 1
  return array, tries
data2 = [10, 8, 2, 5, 6, 7, 4, 3, 1, 9]
print(selection_sort_while(data2))