# SELECTION SORT
#
# Algorithm:
#
# 1 - Find minimum element in the unsorted part of the array
# 2 - Move that element to the sorted part of the array (at the end)
# 3 - Repeat 1 and 2 until sorted
#
# Time complexity: O(n^2)

n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    min_element = arr[i]
    min_index = i
    for j in range(i, len(arr)):
        if min_element > arr[j]:
            min_element = arr[j]
            min_index = j
    temp = arr[i]
    arr[i] = min_element
    arr[min_index] = temp

print(" ".join(str(x) for x in arr))