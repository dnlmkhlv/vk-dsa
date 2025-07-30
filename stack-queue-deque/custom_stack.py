class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def print_stack(self):
        print(self.items)

    
# my_stack = Stack()

# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# my_stack.print_stack()

# my_stack.pop()
# my_stack.print_stack()