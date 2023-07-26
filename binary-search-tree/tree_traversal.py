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

# test in-order DFS method
# should return [18, 21, 27, 47, 52, 76, 82]
print("\nIn-order DFS List: ", my_tree.dfs_in_order())

# test kth smallest method
print("\nkth Smallest Test:")
# should return 18
print("The 1st smallest = ", my_tree.kth_smallest(1))
# should return 27
print("The 3rd smallest = ", my_tree.kth_smallest(3))
# should return 76
print("The 6th smallest = ", my_tree.kth_smallest(6))