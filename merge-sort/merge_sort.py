# merge method merges two lists into one sorted list
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined
    
# merge sort method to sort a list
def merge_sort(list):
    if len(list) == 1:
        return list
    mid_index = int(len(list) / 2)
    left = merge_sort(list[:mid_index])
    right = merge_sort(list[mid_index:])
    return merge(left, right)


# test merge sort
original_list = [3,1,4,2]
sorted_list = merge_sort(original_list)

print("Original List: ", original_list)
print("\nSorted List: ", sorted_list)