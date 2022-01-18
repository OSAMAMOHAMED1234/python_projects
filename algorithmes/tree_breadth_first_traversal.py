tree = {
  '0' : ['1', '2', '3'],
  '1' : ['4', '5'],
  '2' : ['6'],
  '3' : ['7', '8'],
  '4' : [],
  '5' : ['9', '10'],
  '6' : [],
  '7' : [],
  '8' : ['11', '12'],
  '9' : [],
  '10' : [],
  '11' : [],
  '12' : ['18'],
  '18' : [],
}
def breadth_first_traversal(tree, node):
  visited, queue = [], []
  visited.append(node)
  queue.append(node)
  while queue:
    current_queue = queue.pop(0)
    for sibling in tree[current_queue]:
      if sibling not in visited:
        visited.append(sibling)
        queue.append(sibling)
  return visited
print(breadth_first_traversal(tree, '0'))