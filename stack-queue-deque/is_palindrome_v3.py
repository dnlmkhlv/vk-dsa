from custom_deque import Deque

def is_palindrome(s):
    deque = Deque()
    
    for char in s:
        deque.add_rear(char)

    while deque.size() > 1:
        front = deque.remove_front()
        rear = deque.remove_rear()
        if front != rear:
            return False

    return True

# Example usage
print(is_palindrome("abcba"))   # True
print(is_palindrome("daniil"))  # False
print(is_palindrome(""))        # True
print(is_palindrome("abba"))    # True