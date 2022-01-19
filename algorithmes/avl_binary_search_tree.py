class Node(object):
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.height = 1

class AVLTree(object):
  def insert_node(self, root, key):
    if not root:
      return Node(key)
    elif key < root.key:
      root.left = self.insert_node(root.left, key)
    else:
      root.right = self.insert_node(root.right, key)
    root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
    balanceFactor = self.getBalance(root)
    if balanceFactor > 1:
      if key < root.left.key:
        return self.right_rotate(root)
      else:
        root.left = self.left_rotate(root.left)
        return self.right_rotate(root)
    if balanceFactor < -1:
      if key > root.right.key:
        return self.left_rotate(root)
      else:
        root.right = self.right_rotate(root.right)
        return self.left_rotate(root)
    return root

  def delete_node(self, root, key):
    if not root:
      return root
    elif key < root.key:
      root.left = self.delete_node(root.left, key)
    elif key > root.key:
      root.right = self.delete_node(root.right, key)
    else:
      if root.left is None:
        temp = root.right
        root = None
        return temp
      elif root.right is None:
        temp = root.left
        root = None
        return temp
      temp = self.get_min_value_node(root.right)
      root.key = temp.key
      root.right = self.delete_node(root.right, temp.key)
    if root is None:
      return root
    root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
    balanceFactor = self.getBalance(root)
    if balanceFactor > 1:
      if self.getBalance(root.left) >= 0:
        return self.right_rotate(root)
      else:
        root.left = self.left_rotate(root.left)
        return self.right_rotate(root)
    if balanceFactor < -1:
      if self.getBalance(root.right) <= 0:
        return self.left_rotate(root)
      else:
        root.right = self.right_rotate(root.right)
        return self.left_rotate(root)
    return root

  def left_rotate(self, z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
    return y

  def right_rotate(self, z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
    return y

  def get_height(self, root):
    if not root:
      return 0
    return root.height

  def getBalance(self, root):
    if not root:
      return 0
    return self.get_height(root.left) - self.get_height(root.right)

  def get_min_value_node(self, root):
    if root is None or root.left is None:
      return root
    return self.get_min_value_node(root.left)

  def pre_order(self, root):
    if not root:
      return
    print('{0} '.format(root.key), end='')
    self.pre_order(root.left)
    self.pre_order(root.right)

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
      print(currPtr.key)
      self.print_tree(currPtr.left, indent, False)
      self.print_tree(currPtr.right, indent, True)

myTree, root, nums = AVLTree(), None, [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
  root = myTree.insert_node(root, num)
myTree.print_tree(root, '', True)
root = myTree.delete_node(root, 13)
myTree.print_tree(root, '', True)