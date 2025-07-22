n = int(input())
arr = list(map(int, input().split()))

nums = {}

for num in arr:
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1


flag = False

for key, value in nums.items():
    if value > len(arr) // 2:
        print(key)
        flag = True

if flag == False:
    print(-1)