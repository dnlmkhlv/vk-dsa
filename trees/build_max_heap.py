def buildMaxHeap(data):
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        siftDown(data, n, i)
    
def siftDown(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        siftDown(data, n, largest)

arr = [12, 11, 13, 5, 6, 7, 21, 16]
buildMaxHeap(arr)
print(arr)