from stack import Stack

# initial constructor a LinkedList
my_stack = Stack(3)
print("Initial Constructor")
my_stack.print_stack()

# push additional Nodes
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
print("\nPush")
my_stack.print_stack()

# pop Node off of stack
print("\nPopped Node")
print(my_stack.pop().value)
print("\nRemaining Stack")
my_stack.print_stack()