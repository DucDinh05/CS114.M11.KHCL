
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
    
data = int(input())
root = Node(data)
while True:
  x = int(input())
  if x == 0:
    break
  root.Insert(x)

def Demla(Node): 
    if Node is None: 
        return 0 
    if(Node.left is None and Node.right is None): 
        return 1 
    else: 
        return Demla(Node.left) + Demla(Node.right) 

num = Demla(root)
print(num)