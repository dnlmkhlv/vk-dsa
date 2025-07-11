class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)  # O(n) operation

    def add_rear(self, item):
        self.items.append(item)     # O(1) operation

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)  # O(n) operation

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()   # O(1) operation

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print_deque(self):
        print(self.items)
