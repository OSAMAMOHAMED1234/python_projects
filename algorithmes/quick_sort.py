def quick_sort(array):
  length = len(array)
  if length < 2:
    return array
  index = 0
  for i in range(1, length):
    if array[i] <= array[0]:
      index += 1
      array[i], array[index] = array[index], array[i]
  array[0], array[index] = array[index], array[0]
  return quick_sort(array[:index]) + [array[index]] + quick_sort(array[index + 1 : length])
data = [10, 8, 2, 5, 6, 7, 4, 3, 1, 9]
print(quick_sort(data))