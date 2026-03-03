# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def isSameDfs(p, q):
            if not q and not p:
                return True
            if not q or not p or q.val != p.val:
                return False
            
            return isSameDfs(p.left, q.left) and isSameDfs(p.right, q.right)
        
        return isSameDfs(p, q)
        
