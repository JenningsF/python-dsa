from doubly_linked_list import DoublyLinkedList

# initial constructor a LinkedList
my_dll = DoublyLinkedList(3)
print("Initial Constructor")
print(my_dll)

# append and prepend additional Nodes
my_dll.append(4)
my_dll.prepend(2)
my_dll.prepend(1)
my_dll.append(5)
my_dll.append(6)
print("\nAppend & Prepend")
print(my_dll)

my_dll.pop()
my_dll.pop_first()
print("\nPop and Pop First")
print(my_dll)

print("\nGet (2)")
print(my_dll.get(2))
print(my_dll.get(2).value)

my_dll.set_value(0,7)
print("\nSet Value")
print(my_dll)

# my_dll.insert(1,3)
# print("\nInsert")
# print(my_dll)

# my_dll.remove(2)
# print("\nRemove")
# print(my_dll)

# my_dll.reverse()
# print("\nReverse")
# print(my_dll)
