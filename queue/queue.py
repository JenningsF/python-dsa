# class for a Queue Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    # method to print a Node
    def print_node(self):
        if self.next:
            return str(self.value) + " -> " + self.next.print_node()
        else:
            return str(self.value) + " -> None"

# class for implementing a Queue
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    # print() method for a Queue
    def __str__(self):
        if self.first:
            return self.first.print_node()
        else:
            return "None"

    # create new Node and add it to the end of the Queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next= new_node
            self.last = new_node
        self.length += 1

    # remove the first Node in the Queue and return it
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp