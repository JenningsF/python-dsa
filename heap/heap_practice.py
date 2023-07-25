from heap import MaxHeap

# initial Heap constructor
my_heap = MaxHeap()
print("Initial constructor")
print(my_heap.heap)

# inserts values into the Heap
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)
print("\nHeap inserts")
print(my_heap.heap)

# testing the insert of a new max value
my_heap.insert(100)
print("\nNew max insert (100)")
print(my_heap.heap)

# test inert of new non-max value
my_heap.insert(75)
print("\nNew non-max insert (75)")
print(my_heap.heap)

