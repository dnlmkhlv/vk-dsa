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


tree = buildTree([8, 9, 11, 7, 16, 3, 1])
printTree(tree)