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

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

print(exponential_search(arr, target)[0], exponential_search(arr, target)[1])