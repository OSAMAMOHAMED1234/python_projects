def BFS_SP(graph, start, goal):
	explored = []
	queue = [[start]]
	if start == goal:
		print('Same Node')
		return
	while queue:
		path = queue.pop(0)
		node = path[-1]
		if node not in explored:
			neighbours = graph[node]
			for neighbour in neighbours:
				new_path = list(path)
				new_path.append(neighbour)
				queue.append(new_path)
				if neighbour == goal:
					print(*new_path)
					return
			explored.append(node)
	print("So sorry, but a connecting, path doesn't exist :(")
	return

graph = {
  'A': ['B', 'E', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'F', 'G'],
  'D': ['B', 'E'],
  'E': ['A', 'B', 'D'],
  'F': ['C'],
  'G': ['C'],
}
BFS_SP(graph, 'A', 'D')