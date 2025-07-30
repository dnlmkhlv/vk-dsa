def find_sqrt(num):
    left = 0
    right = num

    while left <= right:
        middle = (left + right) // 2
        square = middle * middle

        if square == num:
            return middle
        elif square < num:
            left = middle + 1
        else:
            right = middle - 1

    return right

print(find_sqrt(21)) # 4
print(find_sqrt(16)) # 4