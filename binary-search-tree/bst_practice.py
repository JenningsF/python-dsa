import random

from binary_search_tree import BinarySearchTree

# initial constructor of a Binary Search Tree (BST)
my_tree = BinarySearchTree()
print("\nInitial Constructor")
my_tree.display()

# insert 50 random nodes into BST
for _ in range(15):
    my_tree.insert(random.randint(0,100))
print("\nInsert Nodes")
my_tree.display()
