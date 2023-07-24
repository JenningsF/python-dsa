# Note: Binary Search Tree = BST

# class for a BST Node
class Node:
    # Node constructor
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# class implementing a BST
class BinarySearchTree:
    # BST constructor
    def __init__(self):
        self.root = None