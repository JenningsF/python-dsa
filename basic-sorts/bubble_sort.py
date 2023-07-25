# Bubble Sort algorithm to sort a passed list
def bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

# testing bubble_sort
my_list = [4,2,6,5,1,3]

print("Original List:")
print(my_list)
print("\nBubble Sorted List:")
print(bubble_sort(my_list))