# To search a binary search tree 


class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def search(root,key):
    if root is None or root.data==key
        return root
    elif root.data< key:
        return search(root.right, key)
    else:
        return search(root.left)




