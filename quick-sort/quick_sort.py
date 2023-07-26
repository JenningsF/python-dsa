# swap helper method to swap to values in a list
def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

# pivot helper method
def pivot(list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if list[i] < list[pivot_index]:
            swap_index += 1
            swap(list, swap_index, i)
    swap(list, pivot_index, swap_index)
    return swap_index

# recursive quick sort helper method
def quick_sort_helper(list, left, right):
    if left < right:
        pivot_index = pivot(list, left, right)
        quick_sort_helper(list, left, pivot_index - 1)
        quick_sort_helper(list, pivot_index + 1, right)
    return list

#  quick sort method to sort a list
def quick_sort(list):
    return quick_sort_helper(list, 0, len(list) - 1)

# test quick sort
original_list = [4,6,1,7,3,2,5]
print("Original List: ", original_list)
sorted_list = quick_sort(original_list)
print("\nSorted List: ", sorted_list)