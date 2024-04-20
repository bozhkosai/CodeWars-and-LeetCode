"""delete"""
class TreeNode:
    """class"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """class"""
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif root.val == key:
                if root.right is None:
                    return root.left
                if root.left is None:
                    return root.right
                if root.left and root.right:
                    new = root.right
                    while new.left is not None:
                        new = new.left
                    root.val = new.val
                    root.right = self.deleteNode(root.right, root.val)
            return root
        return None
