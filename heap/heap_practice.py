from heap import MaxHeap

# initial Heap constructor
my_heap = MaxHeap()
print("Initial constructor")
print(my_heap.heap)

# inserts values into the Heap
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
print("\nHeap inserts")
print(my_heap.heap)

# testing the insert of a new max value
my_heap.insert(95)
print("\nNew max insert (95)")
print(my_heap.heap)

# test the insert of new non-max value
my_heap.insert(65)
print("\nNew non-max insert (65)")
print(my_heap.heap)

# test the remove mehotd
my_heap.remove()
print("\nRemove")
print(my_heap.heap)
my_heap.remove()
print(my_heap.heap)