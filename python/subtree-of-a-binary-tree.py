# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameDfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameDfs(self, root, sub):
            if not root and not sub:
                return True
            if root and sub and root.val == sub.val:
                return self.isSameDfs(root.right, sub.right) and self.isSameDfs(root.left, sub.left)
            return False
        
