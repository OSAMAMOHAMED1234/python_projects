def merge_sort(array):
  if len(array) > 1:
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    i, j, array = 0, 0, []
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        array.append(left[i])
        i += 1
      else:
        array.append(right[j])
        j += 1
    array.extend(left[i:])
    array.extend(right[j:])
    return array
  return array
data = [10, 8, 2, 5, 6, 7, 4, 3, 1, 9]
print(merge_sort(data))


def merge_sort(array):
  if len(array) > 1:
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        array[k] = left[i]
        i += 1
      else:
        array[k] = right[j]
        j += 1
      k += 1
    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1
    return array
data = [10, 8, 2, 5, 6, 7, 4, 3, 1, 9]
print(merge_sort(data))