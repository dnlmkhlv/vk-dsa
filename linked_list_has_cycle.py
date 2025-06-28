class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

node3.next = node1

head = node1

print("Has cycle? --> ", hasCycle(head))

node3.next = None

print("Has cycle? --> ", hasCycle(head))