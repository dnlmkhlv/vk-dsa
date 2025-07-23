def hash(l):
    result = ord(l[0])
    x = 31
    q = 2147483647
    for i in range(len(l) - 1):
        result = result * x + ord(l[i + 1])
    return result % q

def rabin_karp(text, pattern):
    x = 31
    q = 2147483647
    pattern_hash = hash(pattern)
    m = len(pattern)

    current_hash = hash(text[0:m])
    i = 0
    while True:
        if pattern_hash == current_hash:
            if pattern == text[i:i + m]:
                return i
        if i + m >= len(text):
            break
        current_hash = ((current_hash - ord(text[i]) * x ** (m-1)) * x + ord(text[i + m])) % q
        i = i + 1
    return None

print(rabin_karp("Short and sweet", "sweet"))