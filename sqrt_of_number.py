def find_sqrt(num):
    arr = []
    for i in range(num + 1):
        arr.append(i)

    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if (arr[middle] ** 2 == num):
            return arr[middle]

        if arr[middle] ** 2 > num:
            right = middle - 1
        else:
            left = middle + 1

    return right

print(find_sqrt(21)) # 4
print(find_sqrt(16)) # 4