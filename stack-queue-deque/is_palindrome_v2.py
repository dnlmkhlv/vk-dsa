from custom_stack import Stack

# Using Stack

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    stack = Stack()
    
    for char in cleaned:
        stack.push(char)

    for char in cleaned:
        if char != stack.pop():
            return False
    return True
    
print(is_palindrome("abcba"))
print(is_palindrome("daniil"))