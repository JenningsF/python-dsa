from binary_search_tree import BinarySearchTree

# initial constructor of a Binary Search Tree (BST)
my_tree = BinarySearchTree()
print(my_tree.root)

# insert nodes into BST
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)