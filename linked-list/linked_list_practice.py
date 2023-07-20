from linked_list import LinkedList

# initial constructor a LinkedList
my_linked_list = LinkedList(3)
print("Initial Constructor")
print(my_linked_list)

# append and prepend additional Nodes
my_linked_list.append(4)
my_linked_list.prepend(2)
my_linked_list.prepend(1)
my_linked_list.append(5)
my_linked_list.append(6)
print("\nAppend & Prepend")
print(my_linked_list)

my_linked_list.pop()
my_linked_list.pop_first()
print("\nPop and Pop First")
print(my_linked_list)


print("\nGet (2)")
print(my_linked_list.get(2))
print(my_linked_list.get(2).value)


my_linked_list.set_value(0,2)
print("\nSet Value")
print(my_linked_list)

my_linked_list.insert(1,3)
print("\nInsert")
print(my_linked_list)

my_linked_list.remove(2)
print("\nRemove")
print(my_linked_list)

my_linked_list.reverse()
print("\nReverse")
print(my_linked_list)

