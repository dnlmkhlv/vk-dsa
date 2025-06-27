n = int(input())

nums = list(map(int, input().split()))

min = abs(nums[0] - nums[1])
num1, num2 = nums[0], nums[1]

for i in range(len(nums) - 1):
    if abs(nums[i] - nums[i + 1]) < min:
        min = abs(nums[i] - nums[i + 1])
        num1, num2 = nums[i], nums[i + 1]

print(f"{num1} {num2}")