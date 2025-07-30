from custom_queue import Queue

def is_subsequence(s: str, t: str) -> bool:
    queue = Queue()

    for char in s:
        queue.enqueue(char)

    for char in t:
        if not queue.is_empty() and char == queue.front():
            queue.dequeue()
        if queue.is_empty():
            return True

    return queue.is_empty()


# Example usage:
if __name__ == "__main__":
    print(is_subsequence("abc", "ahbgdc"))  # True
    print(is_subsequence("axc", "ahbgdc"))  # False
