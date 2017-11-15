""" Introduction to Binary Tree """

class Node:
    def __init__(self, data):
        self.right=None
        self.left=None
        self.key=data



root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)

