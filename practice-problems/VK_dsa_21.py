n = int(input())
arr = list(map(int, input().split()))
target = int(input())

res = -1
left = 0
right = len(arr) - 1

while left <= right:
    middle = left + (right - left) // 2
    if arr[middle] == target:
        res = middle
        break
    if arr[middle] < target:
        left = middle + 1
    else:
        right = middle - 1

if res != -1:
    print(res)
else:
    res = left
    print(res)