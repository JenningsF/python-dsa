# Selection Sort algorithm to sort a passed list
def selection_sort(list):
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        if i != min_index:
            temp = list[i]
            list[i] = list[min_index]
            list[min_index] = temp

    return list

# testing bubble_sort
my_list = [4,2,6,5,1,3]

print("Original List:")
print(my_list)
print("\nSelection Sorted List:")
print(selection_sort(my_list))