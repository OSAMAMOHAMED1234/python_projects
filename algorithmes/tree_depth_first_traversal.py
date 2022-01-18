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
visited = []
def depth_first_traversal(tree, node):
  if node not in visited:
    visited.append(node)
    for sibling in tree[node]:
      depth_first_traversal(tree, sibling)
  return visited
print(depth_first_traversal(tree, '0'))