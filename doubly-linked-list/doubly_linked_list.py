# class for a linked list Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    # method to print a Node
    def print_node(self):
        if self.next:
            return str(self.value) + " - " + self.next.print_node()
        else:
            return str(self.value)

# class implementing a Doubly Linked List
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # print() method for a DoublyLinkedList
    def __str__(self):
        if self.head:
            return self.head.print_node()
        else:
            return "None"
    
    # create new Node and add it to the end of the Doubly Linked List
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

    # remove the last Node in the Doubly Linked List and returns it
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

    # create new Node and add it to the beginning of the Doubly Linked List
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    # remove the first Node in the Doubly Linked List and returns it
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    # return the value of a Node at a specified index within the Doubly Linked List
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    # sets the value of a Node at a specified index as the specified value
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # create new Node and add it to the specified index of the Doubly Linked List
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    # remove the Node at a specified index in the Doubly Linked List and returns it
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
