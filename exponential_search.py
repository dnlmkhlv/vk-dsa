def exponential_search(data, target):
    border = 1
    lastElement = len(data) - 1

    while border < lastElement and data[border] < target:
        if data[border] == target:
            return [border, border * 2]
        
        border = border * 2

        if border > lastElement:
            return [border // 2, lastElement]
        
    return [border // 2, border]

print(exponential_search([3, 4, 7, 9, 11, 12, 18, 24, 63, 72, 81, 99], 18))