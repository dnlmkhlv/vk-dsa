from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(arr, i=0):
    if i >= len(arr):
        return None
    root = TreeNode(arr[i])
    root.left = buildTree(arr, 2 * i + 1)
    root.right = buildTree(arr, 2 * i + 2)
    return root

def printTree(node, level=0, prefix="Root: "):
    if node:
        print(" " * (level * 4) + prefix + str(node.val))
        printTree(node.left, level + 1, "L--- ")
        printTree(node.right, level + 1, "R--- ")

def symmetricTree(root):
    if root is None:
        return True

    queue = deque()
    queue.append((root.left, root.right))

    while queue:
        left, right = queue.popleft()

        if not left and not right:
            continue
        if not left or not right or left.val != right.val:
            return False

        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True

# Example
arr = [1, 2, 2, 3, 4, 4, 3]
tree = buildTree(arr)
printTree(tree)
print("Is symmetric?", symmetricTree(tree))  # Output: True
