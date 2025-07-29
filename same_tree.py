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

def sameTree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.val != b.val:
        return False
    return sameTree(a.left, b.left) and sameTree(a.right, b.right)

tree = buildTree([8, 9, 11, 7, 16, 3, 1])
tree2 = buildTree([8, 9, 11, 7, 16, 3, 1])
print(sameTree(tree, tree2))


tree = buildTree([8, 9, 11, 7, 16, 3, 1])
tree2 = buildTree([8, 9, 11, 7, 16, 3, 1, 2, 3, 4, 5, 6])
print(sameTree(tree, tree2))