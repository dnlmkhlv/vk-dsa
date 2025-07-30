def ternary_search(data, left, right, target):
    if right >= left:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3

        if data[m1] == target:
            return m1
        
        if data[m2] == target:
            return m2
        
        if target < data[m1]:
            return ternary_search(data, left, m1 - 1, target)
        elif target > data[m2]:
            return ternary_search(data, m2 + 1, right, target)
        else:
            return ternary_search(data, m1 + 1, m2 - 1, target)
    return -1

print(ternary_search([3, 8, 9, 11, 12, 16, 18, 19, 21, 24, 27, 29], 0, 11, 16)) # 5