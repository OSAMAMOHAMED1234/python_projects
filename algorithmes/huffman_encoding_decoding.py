class Node:
  def __init__(self, char='', left=None, right=None, freq=0):
    self.char = char
    self.left = left
    self.right = right
    self.freq = freq

  def to_binary(self):
    return '{:08b}'.format(ord(self.char))

  def is_leaf(self):
    return (self.left is None and self.right is None)

  def __lt__(a, b):
    return a.char < b.char

  def __eq__(self, other):
    if isinstance(other, Node):
      return (
        (self.char == other.char) and
        (self.left == other.left) and
        (self.right == other.right)
      )
    return False

  def __repr__(self):
    return 'None' if self.char is None else self.char

def build_tree(text):
  from collections import Counter
  from heapq import heappush, heappop
  char_count = Counter(text)
  queue = []
  for char, freq in char_count.items():
    node = Node(char=char, freq=freq)
    heappush(queue, (node.freq, node))
  while len(queue) > 1:
    freq1, node1 = heappop(queue)
    freq2, node2 = heappop(queue)
    parent_node = Node(
      left = node1,
      right = node2,
      freq = freq1 + freq2
    )
    heappush(queue, (parent_node.freq, parent_node))
  freq, root_node = heappop(queue)
  return root_node

def build_code_table(node):
  table = {}
  def map_char_to_code(node, value):
    if node.is_leaf():
      table[node.char] = value
      return
    map_char_to_code(node.left, value + '0')
    map_char_to_code(node.right, value + '1')
  map_char_to_code(node, '')
  return table

def serialize_tree_to_binary(node): 
  if not node:
    return ''
  if node.is_leaf():
    return '1' + node.to_binary()
  return '0' + serialize_tree_to_binary(node.left) + serialize_tree_to_binary(node.right)

def encode_text(table, text):
  output = ''
  for x in text:
    output += table[x]
  return output

def huffman_encoding(text):
  tree = build_tree(text)
  table = build_code_table(tree)
  trie_bits = serialize_tree_to_binary(tree)
  header = '{:016b}{}'.format(len(trie_bits), trie_bits)
  body = encode_text(table, text)
  return header + body


def deserialize_binary_tree(bits):
  def read_bits(curr_pos):
    if curr_pos >= len(bits):
      return None, curr_pos
    bit = bits[curr_pos]
    if bit == '1':
      char_range_left = curr_pos + 1
      char_range_right = char_range_left + 8
      char_bits = bits[char_range_left : char_range_right]
      return Node(
        char = chr(int(char_bits, 2))
      ), char_range_right
    left_node, pos = read_bits(curr_pos + 1)
    right_node, pos = read_bits(pos)
    return Node(
      left = left_node,
      right = right_node
    ), pos
  node, pos = read_bits(0)
  return node

def decode_text(node, data):
  out = ''
  root = node
  curr_node = root
  for bit in data:
    if bit == '0':
      curr_node = curr_node.left
    else:
      curr_node = curr_node.right
    if curr_node.is_leaf():
      out += curr_node.char
      curr_node = root
  return out

def huffman_decoding(bit_string):
  tree_size = int(f'{bit_string[0:16]}', 2)
  tree_range_end = 16 + tree_size
  tree = deserialize_binary_tree(bit_string[16 : tree_range_end])
  body = bit_string[tree_range_end:]
  return decode_text(tree, body)

string = 'My name is OSAMA, I love Egypt.'
en_string = huffman_encoding(string)
de_string = huffman_decoding(en_string)
print(en_string)
print(de_string)