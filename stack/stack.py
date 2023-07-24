# class for a Stack Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# class for implementing a Stack
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    # prints out contents of a Stack
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    # create new Node and add it to the top of the Stack
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    # remove the top Node in the Stack and return it
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp    
        