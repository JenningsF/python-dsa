from queue import Queue

# initial constructor a LinkedList
my_queue = Queue(3)
print("Initial Constructor")
print(my_queue)

# enqueue additional Nodes to Queue
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)
print("\nEnqueue")
print(my_queue)

# dequeue Node off of Queue
print("\nDequeue all Nodes")
while my_queue.length > 0:
    print("\nDequeued Node:")
    print(my_queue.dequeue().value)
    print("Remaining Queue")
    print(my_queue)