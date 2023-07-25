# Insertion Sort algorithm to sort a passed list
def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while temp < list[j] and j > -1:
            list[j + 1] = list[j]
            list[j] = temp
            j -= 1
    return list

# testing bubble_sort
my_list = [4,2,6,5,1,3]

print("Original List:")
print(my_list)
print("\nInsertion Sorted List:")
print(insertion_sort(my_list))