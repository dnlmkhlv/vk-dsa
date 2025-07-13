def binarySearchCheck(data, target):
    left = 0
    right = len(data) - 1

    if (data[left] > target) or (data[right] < target):
        return -1
    
    return binarySearch(data, target, left, right)

def binarySearch(data, target, left, right):
    if left > right:
        return -1
    
    middle = (left + right) // 2

    if data[middle] == target:
        return middle

    if data[middle] < target:
        return binarySearch(data, target, middle + 1, right)
    else:
        return binarySearch(data, target, left, middle - 1)


    

print(binarySearchCheck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))