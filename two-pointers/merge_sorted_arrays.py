def merge_sorted_arrays(arr1, arr2):
    merged_arr = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            merged_arr.append(arr2[j])
            j += 1
        else:
            merged_arr.append(arr1[i])
            i += 1
            j += 1

    merged_arr.extend(arr1[i:])
    merged_arr.extend(arr2[j:])

    return merged_arr


arr1 = [1, 4, 9]
arr2 = [2, 6, 8]
merged_arr = merge_sorted_arrays(arr1, arr2)

print(merged_arr)
