def target_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        res = arr[left] + arr[right]
        if res == target:
            return arr[left], arr[right]
        elif res < target:
            left += 1
        else:
            right -= 1

print(target_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 17))
print(target_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))