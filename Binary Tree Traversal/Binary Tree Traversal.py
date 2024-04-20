"""traversal"""
class Node:
    """class"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node):
    """pre-order"""
    if not node:
        return []
    return [node.value] + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    """in-order"""
    if not node:
        return []
    return in_order(node.left) + [node.value] + in_order(node.right)

# Post-order traversal
def post_order(node):
    """post-order"""
    if not node:
        return []
    return post_order(node.left) +  post_order(node.right) + [node.value]
