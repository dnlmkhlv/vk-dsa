class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

def reverse_linked_list(head):
    prev = None
    curr = head

    print(curr)

    while curr != None:
        next_node = curr.next  # Save next node
        curr.next = prev       # Reverse the link
        prev = curr            # Move prev forward
        curr = next_node       # Move curr forward

        print(curr)

    return prev  # New head of the reversed list

# Helper to print list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating a sample list: 1 -> 2 -> 3
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

print("Original:")
print_list(node1)
print()

reversed_head = reverse_linked_list(node1)

print()
print("Reversed:")
print_list(reversed_head)