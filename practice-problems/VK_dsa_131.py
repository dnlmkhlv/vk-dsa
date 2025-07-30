N = int(input())

arr = list(map(int, input().split()))

new_arr = [x for x in arr if x != 0 ] + [0]* arr.count(0)

print(' '.join(map(str, new_arr)))