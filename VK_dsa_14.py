n = int(input())
arr = list(map(int, input().split()))

max = arr[0]

for x in arr:
    if x > max:
        max = x

print(max)