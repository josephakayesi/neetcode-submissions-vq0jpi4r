# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        - Start at root and swap every subtree recrusively. 
        - Stop when you are at a leaf node
        """

        def dfs(node):
            if not node:
                return 
            
            node.left, node.right = node.right, node.left 

            dfs(node.left)
            dfs(node.right) 

        dfs(root)

        return root