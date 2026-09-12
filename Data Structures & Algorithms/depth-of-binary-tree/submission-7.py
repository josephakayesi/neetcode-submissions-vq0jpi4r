# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         res = 0

#         def dfs(node, depth):
#             nonlocal res

#             if not node:
#                 return 

#             res = max(res, depth)
#             dfs(node.left, depth + 1)
#             dfs(node.right, depth + 1)
#             return 
        
#         dfs(root, 1)
        
#         return res

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

