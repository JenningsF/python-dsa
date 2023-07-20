class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def print_node(self):
        if self.next:
            return str(self.value) + " - " + self.next.print_node()
        else:
            return str(self.value)


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def __str__(self):
        if self.head:
            return self.head.print_node()
        else:
            return "None"
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
