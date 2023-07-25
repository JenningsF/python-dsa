# import random

from binary_search_tree import BinarySearchTree

# initial constructor of a Binary Search Tree (BST)
my_tree = BinarySearchTree()
print("\nInitial Constructor")
my_tree.display()

# insert 50 random nodes into BST
# for _ in range(15):
#     my_tree.insert(random.randint(0,100))

# insert 7 specific nodes into BST
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print("\nInsert Nodes")
my_tree.display()

# find specific node in BST using contains
print("\nBasic contains")
print("Is 27 in the BST?")
print(my_tree.contains(27))
print("Is 17 in the BST?")
print(my_tree.contains(17))

# test recursive contains method
print("\nRecursive contains")
print("Is 27 in the BST?")
print(my_tree.r_contains(27))
print("Is 17 in the BST?")
print(my_tree.r_contains(17))