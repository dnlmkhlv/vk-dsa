def extraLetter(a, b):
    hashmap_b = {}

    for char in b:
        if char in hashmap_b:
            hashmap_b[char] += 1
        else:
            hashmap_b[char] = 1

    for char in a:
        if char in hashmap_b and hashmap_b[char] > 0:
            hashmap_b[char] -= 1

    for char, count in hashmap_b.items():
        if count > 0:
            return char
        
    return ""


print(extraLetter("uio", "oeiu"))
print(extraLetter("daniil", "adaniil"))