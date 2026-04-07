# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        - For equivalence:
        - Iterate through all nodes of p and q in the same order. 
        - If any nodes differ in value then return False
        - Otherwise return True once exhausted check
        """

        if not p and not q:
            return True 

        if not p or not q:
            return False
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
        return False