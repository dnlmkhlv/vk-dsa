from itertools import combinations
import math

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# Выбираем все возможные комбинации из k элементов
max_product = -math.inf
for comb in combinations(arr, k):
    product = 1
    for num in comb:
        product *= num
    max_product = max(max_product, product)

print(max_product)
