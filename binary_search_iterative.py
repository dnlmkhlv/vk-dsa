def binarySearch(data, target):
    left = 0
    right = len(data) - 1

    if data[left] > target or data[right] < target:
        return -1

    if left > right:
        return - 1


    while left <= right:
        middle = left + (right - left) // 2

        if data[middle] == target:
            return middle
        
        if target > data[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return -1

print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))