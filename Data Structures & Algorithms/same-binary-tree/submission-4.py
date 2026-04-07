# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        - Start at both roots. 
        - If the values at each node of the two trees are not equal then return False
        - After traversing through the nodes and no inequality is found then return True. i.e same tree 
        """
        
        if not p and not q:
            return True 
        
        if not p or not q:
            return False
            
        while p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False