s = input()
s = s.lower()
store = {}
for char in s:
    if char not in store:
        store[char] = 1
    else:
        store[char] += 1
maxValue = 0
maxKey = s[0]
for key, value in store.items():
    if value > maxValue:
        maxValue = value
        maxKey = key
print(maxValue)