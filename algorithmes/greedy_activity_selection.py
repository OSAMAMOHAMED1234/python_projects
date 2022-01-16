def activity_selection(start, finish):
  i, start, finish, tasks_list = 0, sorted(start), sorted(finish), [0, ]
  for j in range(len(finish)):
    if start[j] >= finish[i]:
      i = j
      tasks_list.append(i)
  return tasks_list
print(activity_selection([12, 10, 20] , [25, 20, 30]))