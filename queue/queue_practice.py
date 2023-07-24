from queue import Queue

# initial constructor a LinkedList
my_queue = Queue(3)
print("Initial Constructor")
print(my_queue)

# enqueue additional Nodes
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)
print("\nEnqueue")
print(my_queue)
