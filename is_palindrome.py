
# Using Two Pointers

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1

    return True

print(is_palindrome("abcba"))
print(is_palindrome("daniil"))