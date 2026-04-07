# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        - Start at the root.
        - Check if the left and right subtree is balanced and then return
        - Go through each node; calculate whether that node is a balanced tree
            - To be balanced:
                - left should be balanced
                - right should be balanced
                - (left - right) <= 1
        - Return True if balanced
        """
        
        if not root:
            return True 
            
        
        def dfs(node):
            if not node:
                return [True, 0]
                
            left = dfs(node.left)
            right = dfs(node.right)
            
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return [balanced, max(left[1], right[1]) + 1]
            
        return dfs(root)[0]