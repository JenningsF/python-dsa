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
# should return [47, 21, 76, 18, 27, 52, 82]
print("\nBFS List: ", my_tree.bfs())

# test pre-order DFS method
# should return [47, 21, 18, 27, 76, 52, 82]
print("\nPre-order DFS List: ", my_tree.dfs_pre_order())

# test post-order DFS method
# should return [18, 27, 21, 52, 82, 76, 47]
print("\nPost-order DFS List: ", my_tree.dfs_post_order())
