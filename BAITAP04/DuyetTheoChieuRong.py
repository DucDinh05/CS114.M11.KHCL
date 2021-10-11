class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent_node = data

    def Insert(self, value):
        if self.parent_node:
            if value < self.parent_node:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.Insert(value)
                
            elif value > self.parent_node:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.Insert(value)
        else:
            self.parent_node = value
    
def height_tree(Node):
	if Node is None:
		return 0
	else:
		left = height_tree(Node.left)
		right = height_tree(Node.right)

	if left > right:
		return left + 1
	else:
		return right + 1

def print_node(root, level):
	if root is None:
		return
	if level == 1:
		print(root.data, end=" ")
	elif level > 1:
		print_node(root.left, level-1)
		print_node(root.right, level-1)

def print_level(root):
	h = height_tree(root)
	for i in range(1, h+1):
		print_node(root, i)
data = int(input())
root = Node(data)
while True:
  x = int(input())
  if x == 0:
    break
  root.Insert(x)

print_level(root)