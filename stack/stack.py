# class for a queue Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# class for implementing a stack
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    # prints out contents of a Stack
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
            