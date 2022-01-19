class Tree:
  def __init__(node, value):
    node.value = value
    node.left = None
    node.right = None

  def inorder(node, root): 
    if root is None:
      return
    node.inorder(root.left)
    print(root.value, end = ' ')
    node.inorder(root.right)

  def Insert(node, value): 
    if node is None:
      node = Tree(value)
    elif value < node.value:
      if node.left is None:
        node.left = Tree(value)
      else:
        node.left.Insert(value)
    else:
      if node.right is None:
        node.right = Tree(value)
      else:
        node.right.Insert(value)

  def delete(node, temp, value): 
    if value < node.value:
      temp = node
      node.left.delete(temp,value)
    elif value > node.value:
      temp = node
      node.right.delete(temp, value)
    else:
      if node.left is None and node.right is None:
        if temp.left == node:
          temp.left = None
        else:
          temp.right = None
        node = None
      elif node.right is None:
        if temp.left == node:
          temp.left = node.left
        else:
          temp.right = node.left
        node = None
      elif node.left is None:
        if temp.left == node:
          temp.left = node.right
        else:
          temp.right = node.right
        node = None
      else:
        temp = node.right
        while temp.left is not None:
          temp = temp.left
        node.value = temp.value
        node.right.delete(temp, temp.value)
  
  def print_tree(self, currPtr, indent, last):
    from sys import stdout
    if currPtr != None:
      stdout.write(indent)
      if last:
        stdout.write('R----')
        indent += '     '
      else:
        stdout.write('L----')
        indent += '|    '
      print(currPtr.value)
      self.print_tree(currPtr.left, indent, False)
      self.print_tree(currPtr.right, indent, True)

Root = Tree(6)
Root.Insert(4)
Root.Insert(2)
Root.Insert(5)
Root.Insert(9)
Root.Insert(8)
Root.Insert(10)
Root.inorder(Root)
Root.delete(Root, 2)
print ('\n 2 is deleted: ',end ='')
Root.inorder(Root)
Root.delete(Root, 4)
print ('\n 4 is deleted: ',end ='')
Root.inorder(Root)
Root.delete(Root, 6)
print ('\n 6 is deleted: ',end ='')
Root.inorder(Root)
print ()
Root.print_tree(Root, '', True) 