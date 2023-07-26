# swap helper method to swap to values in a list
def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

# pivot helper method to
def pivot(list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if list[i] < list[pivot_index]:
            swap_index += 1
            swap(list, swap_index, i)
    swap(list, pivot_index, swap_index)
    return swap_index

# quick sort method to sort a list
def quick_sort(list):
    pass

# test quick sort
original_list = [4,6,1,7,3,2,5]
print("Original List: ", original_list)
# sorted_list = quick_sort(original_list)

# test pivot method
print(pivot(original_list, 0, 6))
print("\nPivoyed List: ", original_list)
# print("\nSorted List: ", sorted_list)