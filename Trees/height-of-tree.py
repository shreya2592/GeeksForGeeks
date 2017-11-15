class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break




def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right))+1



tree=BinarySearchTree()
t= int(input())
for  _ in range 
