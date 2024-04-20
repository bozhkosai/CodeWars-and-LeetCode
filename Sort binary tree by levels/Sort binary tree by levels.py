"""sort"""
from collections import deque
class Node:
    """class"""
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    """tree by levels"""
    if node:
        res = []
        queue = deque([node])
        while queue:
            current = queue.popleft()
            res.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return res
    return []
