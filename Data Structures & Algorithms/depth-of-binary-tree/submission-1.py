# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Thought process
        - Define base case
        - Run dfs recursively on the left and right subtree
        - Return max value between left and right and add 1
        """

        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

"""
            1
        2       3
              4

maxDepth(1) -> 3
    maxDepth(2) -> 1
    maxDepth(3) -> 2
        maxDepth(4) -> 1

"""