n = int(input())

arr = list(map(int, input().split()))

element = int(input())

new_arr = [x for x in arr if x != element]

print(' '.join(map(str, new_arr)))