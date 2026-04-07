# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Intuition:
        - Start at the root
        - Find the height of left subtree and right subtree. 
        - If height differ by one, return false otherwise return 1

                1
            2       3
                4

            dfs(1):
                - dfs(2)
                - dfs(3)
        """


        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


        
        