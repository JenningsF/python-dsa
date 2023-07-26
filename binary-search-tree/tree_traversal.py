from binary_search_tree import BinarySearchTree

# create BST for BFS test
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

my_tree.display()
# test BFS method
print("\nBFS List: ", my_tree.bfs())
# should return [47, 21, 76, 18, 27, 52, 82]
