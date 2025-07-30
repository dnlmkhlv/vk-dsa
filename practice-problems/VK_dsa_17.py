n = int(input())
nums = list(map(int, input().split()))

res = -1

for num in nums:
    if num % 2 == 0:
        res = num

print(res)